# 💼 AFTA Salary Loan Calculator

A modular full-stack application built during the **AFTA Bootcamp**, designed to help users estimate monthly loan repayments based on their salary. The project emphasizes modern development practices including containerization, clean API design, and data analysis using Pandas.


## 🧱 Architecture Diagram

```plaintext
                      ┌──────────────────────┐
                      │    🖥️ Streamlit UI    │
                      │ (Frontend container) │
                      └──────────┬───────────┘
                                 │
                        HTTP API (Loan Data)
                                 │
                      ┌──────────▼───────────┐
                      │     ⚙️ FastAPI API     │
                      │ (Backend container)  │
                      └──────────┬───────────┘
                                 │
                            Internal logic
                                 │
                         Pandas Calculations
                                 │
                      ┌──────────▼───────────┐
                      │   📊 Repayment Logic  │
                      └──────────────────────┘
```

---

## 🔌 API Descriptions

| Method | Endpoint         | Description                           |
|--------|------------------|---------------------------------------|
| POST   | `/calculate`     | Takes salary & loan details, returns monthly repayment |
| GET    | `/health`        | Health check endpoint to confirm backend is running |
| (Optional) | `/docs`     | Auto-generated Swagger UI (FastAPI) for testing APIs |

Example payload for `/calculate`:
```json
{
  "salary": 1200000,
  "loan_amount": 3000000,
  "duration_months": 12
}
```

---

## 🐼 Pandas Explanation

Pandas is used in the backend to perform efficient calculations related to:

- Loan amortization schedules
- Monthly repayment formulas
- Interest calculations

Using Pandas allows us to model loan behavior with greater flexibility and eventually export data to Excel/CSV if needed.

---

## 🛠️ Setup Guide

### ✅ Prerequisites
- Docker & Docker Compose installed
- Python 3.10+ (if running locally without Docker)

### 🚀 Quick Start (Docker)

```bash
# Clone the repo
git clone https://github.com/yourusername/afta-salary-loan.git
cd afta-salary-loan

# Start services
sudo docker-compose up --build
```

Then visit:
- Frontend: `http://localhost:8501`
- API Docs: `http://localhost:8000/docs`

---

### ⚙️ Manual Start (Local Development)

#### 1. Backend (FastAPI)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### 2. Frontend (Streamlit)
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 Technologies Used

- **FastAPI** – High-performance API framework
- **Streamlit** – Simple UI framework for Python
- **Pandas** – Powerful data analysis library
- **Docker** – Containerization
- **Docker Compose** – Multi-container orchestration

---

## 📄 License

MIT License. Feel free to use and modify this project for educational or commercial use.

---