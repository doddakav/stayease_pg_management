🏠 StayEase – PG & Hostel Management System    --- Live demo: https://stayease-pg-management.streamlit.app/

StayEase is a web-based PG and Hostel Management System built to simplify day-to-day property management.

The application has separate experiences for Owners and Tenants. Owners can manage rooms, tenants, payments, and complaints, while tenants can view their stay information, payments, complaints, and profile.

✨ Features

👨‍💼 Owner

Secure login

Dashboard with room, tenant, payment, and complaint information

Add, view, edit, and delete rooms

Add, view, edit, and delete tenants

Add, view, edit, and delete payments

View tenant complaints

Update complaint status

View owner profile

👤 Tenant

Tenant login

Personal dashboard

View payment history

Raise complaints

View own complaints and complaint status

View profile and room information

Change password

🛠️ Technology Stack

Technology

Purpose

Python

Application programming

FastAPI

Backend REST API

Streamlit

Frontend / user interface

Supabase

Database and backend data service

PostgreSQL

Relational database

Uvicorn

FastAPI application server

Git & GitHub

Version control and source code hosting

Render

Backend deployment

Streamlit Community Cloud

Frontend deployment

🏗️ Project Architecture

                    ┌──────────────────────┐
                    │  Streamlit Frontend  │
                    │   Owner / Tenant UI  │
                    └──────────┬───────────┘
                               │ HTTP Requests
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend    │
                    │      REST APIs       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Supabase       │
                    │ PostgreSQL Database  │
                    └──────────────────────┘

📁 Project Structure

PG project/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── login.py
│   │   ├── dashboard.py
│   │   ├── rooms.py
│   │   ├── tenants.py
│   │   ├── tenant.py
│   │   ├── payments.py
│   │   └── complaints.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── api.py
│   ├── requirements.txt
│   └── views/
│       ├── rooms.py
│       ├── tenants.py
│       ├── payments.py
│       ├── complaints.py
│       ├── tenant_dashboard.py
│       ├── tenant_payments.py
│       ├── tenant_complaints.py
│       └── tenant_profile.py
│
└── .gitignore

🗄️ Main Database Entities

The application works with the following main entities:

Users – login and user information

Rooms – room details and occupancy information

Tenants – tenant and stay information

Payments – monthly rent/payment records

Complaints – tenant complaints and their status

The backend uses Supabase to communicate with the PostgreSQL database.

🔄 Application Flow

Owner

Owner Login
     ↓
Owner Dashboard
     ↓
Rooms / Tenants / Payments / Complaints
     ↓
Create / Read / Update / Delete

Tenant

Tenant Login
     ↓
Tenant Dashboard
     ↓
My Payments / My Complaints / My Profile

🚀 Deployment

The application is deployed using:

FastAPI backend: Render

Streamlit frontend: Streamlit Community Cloud

Database: Supabase

Production Architecture

User
 │
 ▼
Streamlit Community Cloud
 │
 ▼
Render FastAPI Backend
 │
 ▼
Supabase PostgreSQL

⚙️ Local Setup

1. Clone the repository

git clone https://github.com/doddakav/stayease_pg_management.git
cd stayease_pg_management

2. Create a Python virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install backend dependencies

cd backend
pip install -r requirements.txt

4. Configure environment variables

Create a .env file inside the backend directory.

Example:

SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key

Do not commit .env to GitHub.

5. Run the FastAPI backend

From the backend directory:

python -m uvicorn app.main:app --reload

The API will normally be available at:

http://127.0.0.1:8000

FastAPI documentation is available at:

http://127.0.0.1:8000/docs

6. Run the Streamlit frontend

Open another terminal from the project root:

streamlit run frontend/app.py

🔐 Environment Variables

The application uses environment variables for Supabase configuration.

Required:

SUPABASE_URL
SUPABASE_KEY

Keep all secret credentials out of source control.

🔒 Current Authentication

The project currently uses mobile number and password based login with separate owner and tenant roles.

The tenant change-password feature is implemented.

bcrypt password hashing is intentionally not included in the current version and can be added as a future security improvement.

📌 Future Improvements

Possible future enhancements include:

Password hashing with bcrypt

Stronger authentication and authorization

Password reset

Email/SMS notifications

Payment receipt generation

Advanced reporting

Search and filtering

Improved validation

Automated tests

Custom domain deployment

🎯 Project Goal

StayEase was built as a practical full-stack project to demonstrate:

REST API development

CRUD operations

Role-based application flow

Database integration

Frontend/backend communication

Cloud deployment

Git and GitHub workflow

👨‍💻 Author

Doddakav

GitHub:
https://github.com/doddakav

📄 License

This project is intended for learning and portfolio purposes.
