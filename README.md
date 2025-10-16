# Backend Wizards — Stage 0: Dynamic Profile Endpoint

[🔗 GitHub Repository](https://github.com/bcorji/backend-wizards-stage0)

A simple RESTful API built with **FastAPI** that returns developer profile information along with a dynamic fact fetched from an external API (e.g., a random cat fact).

---

## 📘 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Configuration / Environment Variables](#configuration--environment-variables)
- [Running Locally](#running-locally)
- [API Endpoint](#api-endpoint)
- [Dependencies](#dependencies)
- [License](#license)

---

## 🚀 Features

- `/me` endpoint returns static profile data + dynamic fact  
- Fetches real-time fact from an external API  
- Proper error handling and logging  
- ISO 8601 timestamp formatting  
- CORS support  
- Configurable environment variables

---

## 🧠 Tech Stack

- **Framework:** FastAPI  
- **Language:** Python 3.8+  
- **Server:** Uvicorn (ASGI)  
- **HTTP Client:** httpx  

---

## ⚙️ Prerequisites

Before running the project, make sure you have:

- Python **3.8 or newer** installed  
- `pip` (Python package manager)  
- Optionally: a virtual environment tool (`venv`, `virtualenv`, or `poetry`)

---

## 🛠 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/bcorji/backend-wizards-stage0.git
   cd backend-wizards-stage0
   ```

2. **(Optional) Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate     # macOS / Linux
   # or
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   ```
Update the .env file with your details

---


## 💻 Running Locally

To start the development server:

```bash
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --reload
```

Then open your browser at:

👉 [http://localhost:8000](http://localhost:8000)

The `--reload` flag enables hot reloading during development.

---

## 📡 API Endpoint

### `GET /me`

Returns basic profile data and a dynamic fact from an external API.

**Example Response:**

```json
{
  "status": "success", 
  "user": {
    "email": "<your email>", 
    "name": "<your full name>", 
    "stack": "<your backend stack>"
  }, 
  "timestamp": "<current UTC time in ISO 8601 format›", 
  "fact": "<random cat fact from Cat Facts API>"
}
```

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`.

Common dependencies include:

- `fastapi`
- `uvicorn`
- `httpx`
- `python-dotenv` *(for environment variables)*

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🪪 License

This project is licensed under the **MIT License**.

---

### 👤 Author

**Bliss Orji**  
[GitHub Profile](https://github.com/bcorji)

---