[# FastAPI_reference_link]
(https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content

# 🚀 FastAPI & Backend Development - Learning Notes

## 1. Core Concepts: The "What" and "Why"

### Frontend vs. Backend
* **Frontend (The Dining Area):** What the user sees (Buttons, Text, Colors).
* **Backend (The Kitchen):** Logic, Database, Security. It processes the request and serves the data.
* **API (The Waiter):** The messenger that takes requests from Frontend to Backend and brings back the food (Data).

### Architecture Styles
* **Monolith (The Mega-Restaurant):**
    * All code (User, Payment, Products) in **one project/folder**.
    * *Pros:* Easy to start, simple debugging.
    * *Cons:* Hard to scale, one error crashes everything.
* **Microservices (The Food Court):**
    * Separate tiny projects for each feature.
    * *Pros:* Scalable, independent.
    * *Cons:* Complex to manage.

---

## 2. The Toolkit: FastAPI, Starlette, & Pydantic

**FastAPI is not an API itself; it is the tool used to build APIs.** It relies on two giant pillars:

1.  **Starlette (The Engine):** Handles the web parts (Routing, Async speed, Server requests).
2.  **Pydantic (The Security Guard):** Handles **Data Validation**. It ensures users send numbers for age, not text.

---

## 3. Environment Setup

### Virtual Environments (`.venv`)
* **Purpose:** A "Toolbox" specifically for one project so dependencies don't conflict.
* **Conda:** Best for AI/Data Science (installs non-Python tools like C++ libraries).
* **Venv:** Standard for pure Python web dev.

### Essential Commands (Windows PowerShell)
| Action | Command |
| :--- | :--- |
| **Create Env** | `python -m venv .venv` |
| **Activate** | `.\.venv\Scripts\activate` |
| **Deactivate** | `deactivate` |
| **Install Libs** | `pip install fastapi uvicorn pydantic` |

> **Tip:** If activation fails, check execution policy: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## 4. FastAPI Code Structure

### Routes (The URLs)
* **Static Routes:** Fixed paths (e.g., `/users/me`). **Always put these FIRST.**
* **Dynamic Routes:** Variable paths (e.g., `/users/{user_id}`).

### Query Parameters & Validation
Using `Query` ensures data quality before your code even runs.

```python
from fastapi import Query

@app.get("/products")
def list_products(
    # "q" is optional, must be 3-50 chars long
    q: str = Query(default=None, min_length=3, max_length=50) 
):
    ...)
