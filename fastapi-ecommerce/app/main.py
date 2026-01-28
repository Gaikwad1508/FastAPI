from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException, Query, Path, Depends, Request
from service.products import (
    get_all_products,
    load_products,
    add_product,
    remove_product,
    change_product,
)
from schema.product import Product, ProductUpdate
from uuid import uuid4, UUID
from datetime import datetime
from typing import List, Dict
from fastapi.responses import JSONResponse

load_dotenv()
app = FastAPI()

# @app.middleware("http")
# async def lifecycle(request: Request, call_next):
#     print("Before request")
#     response = await call_next(request)
#     print("After request")
#     return response

"""
#Static route: A static route is a hard-coded path. It never changes. It matches exactly one specific URL.
@app.get('/')
def root():
    return {"message": 'Welcome to the FastAPI'}

#Dynamic route: A dynamic route uses curly brackets {} to create a "placeholder." It can accept different values in the URL.
@app.get('/products/{id}')
def get_products(id: int):
    products = ["Laptop", "Smartphone", "Mouse", "algebra"]
    return products[id]
"""

# @app.get("/products")
# def get_products():
#     return get_all_products()


def common_logic():
    return "HEllo There"


@app.get("/", response_model=dict)
def root(dep=Depends(common_logic)):
    DB_PATH = os.getenv("BASE_URL")
    # return {"message": "Welcome to FastAPI", "dependency": dep, "data_path": DB_PATH}
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to FastAPI",
            "dependency": dep,
            "data_path": DB_PATH,
        },
    )


##Using query to filterout the records
@app.get("/products", response_model=Dict)
def list_products(
    dep=Depends(
        load_products
    ),  ## Dependency Injection: FastAPI executes 'load_products' and injects the result here.
    name: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search product by name(case Insensitive)",
    ),
    sort_by_price: bool = Query(default=False, description="Sort products by price"),
    order: str = Query(
        default="asc", description="Sort order when sort_by_price = true (asc, desc)"
    ),
    limit: int = Query(
        default=10,
        ge=1,  # Greater than or Equal to (>=)
        le=100,  # Less than or Equal to (<=)
        description="Number of items to return",
    ),
    offset: int = Query(
        default=0,
        ge=0,  # start from this index for further processing
        description="Pagination offset",
    ),
):
    # products = get_all_products()
    products = dep

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code=404, detail=f"No product found matching name = {name}"
        )

    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    total = len(products)
    products = products[offset : offset + limit]
    return {"total": total, "limit": limit, "offset": offset, "items": products}


##Using path to provide some validation to data
@app.get("/products/{product_id}", response_model=Dict)
def get_product_by_id(
    product_id: str = Path(
        ...,
        min_length=36,
        max_length=36,
        description="UUID of the product",
        example="98235fe0-bc3f-4340-f322-cga2e0cad139",
    )
):
    products = get_all_products()
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)
def create_product(product: Product):
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid4())
    product_dict["created_at"] = datetime.utcnow().isoformat() + "Z"
    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product.model_dump(mode="json")


@app.delete("/products/{product_id}")
def delete_product(product_id: UUID = Path(..., description="Product UUID")):
    try:
        res = remove_product(str(product_id))
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/products/{product_id}")
def update_product(
    product_id: UUID = Path(..., description="Product UUID"),
    payload: ProductUpdate = ...,
):
    try:
        update_product = change_product(
            str(product_id), payload.model_dump(mode="json", exclude_unset=True)
        )
        return update_product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
