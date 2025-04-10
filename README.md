# 📝 Task Management System (Django)

A web-based Task Management System built using **Django** and **SQLite** that helps users efficiently create, track, update, and manage their tasks. Features include user authentication (JWT-based), task categorization, and filtering by priority, status, and due date.

---

## 🚀 Features

- ✅ JWT-based **User Authentication** (Register/Login)
- 📋 **CRUD operations** for tasks
- 🗓️ Assign **due dates** to tasks
- 🚦 Task status tracking: `Pending`, `In Progress`, `Completed`
- 🧮 Filter tasks by `status`, `priority`, or `due date`

---

## 📦 Tech Stack

- **Backend:** Django (Python)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Database:** SQLite
- **API:** Django REST Framework (DRF)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/task-management-django.git
cd task-management-django
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

---

## 🔐 API Endpoints

| Method | Endpoint       | Description                         |
| ------ | -------------- | ----------------------------------- |
| POST   | `/register/`   | Register a new user                 |
| POST   | `/login/`      | Authenticate user, return JWT token |
| GET    | `/tasks/`      | Retrieve all tasks (auth required)  |
| POST   | `/tasks/`      | Create a new task                   |
| PUT    | `/tasks/<id>/` | Update a task                       |
| DELETE | `/tasks/<id>/` | Delete a task                       |

---
