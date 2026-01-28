
# 🛒 FastAPI E-Commerce Backend

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-red)

A robust, production-ready REST API for an E-Commerce platform. Built with **FastAPI** to handle product management, data validation, and persistent file-based storage.

---

## 📖 About The Project

This backend service handles the core logic for an online store. It demonstrates modern backend architecture using the **Service-Repository Pattern**.

### Key Features
* ✅ **CRUD Operations:** Create, Read, Update, Delete products efficiently.
* ✅ **Data Validation:** Strict type enforcement using **Pydantic V2**.
* ✅ **Advanced Search:** Filter products by name, sort by price, and pagination.
* ✅ **Business Logic:** Automatic stock validation and discount calculations.
* ✅ **Scalable Structure:** Modular code separated into Schema, Service, and Routes.

> **👨‍💻 Learning Journey:**
> I documented every concept, design decision, and "Why" behind this code.
> 👉 **[Click here to read my detailed LEARNING_NOTES.md](./LEARNING_NOTES.md)**

---

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Server:** Uvicorn
* **Validation:** Pydantic
* **Architecture:** Service-Repository Pattern
* **Storage:** JSON Persistence (Simulated Database)

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```

### 2. Set Up Virtual Environment

```bash
# Create environment
python -m venv .venv

# Activate (Windows)
.\.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment

Create a `.env` file in the root directory:

```properties
BASE_URL=data/products.json

```

### 5. Run the Server

```bash
uvicorn app.main:app --reload

```

The API will be live at: `http://127.0.0.1:8000`

---

## 📚 API Documentation

FastAPI automatically generates interactive documentation.
Once the server is running, visit:

* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

---

## 📂 Project Structure

```text
fastapi-ecommerce/
│
├── app/
│   ├── schema/          # Pydantic Models (Data Validation)
│   ├── service/         # Business Logic & CRUD
│   ├── data/            # JSON Database
│   └── main.py          # API Routes
│
├── LEARNING_NOTES.md    # Detailed concepts & guide
├── .env                 # Environment variables
└── requirements.txt     # Dependencies

```

---

