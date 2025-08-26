# 🛡️ Incident Management System

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An open-source, lightweight **Incident Management System** to log, assign, track, and resolve incidents in IT infrastructure and applications. Built using Python (Flask), SQLite, and Docker, with role-based access, REST APIs, and email notifications via SMTP.

---

## 📌 Features

- 🧑‍💼 **Role-based Access**: Admin, Engineer, Reporter
- 📝 **Incident Logging**: Create, assign, resolve, update
- 🔁 **RESTful APIs**: JSON endpoints for integration
- ✉️ **Email Alerts**: Incident notifications via SMTP
- 💾 **SQLite**: Lightweight and portable database
- 🐳 **Docker Support**: Containerized for easy deployment

---

## 🚀 Live Demo (Optional)

> _📽️ Add screenshots or a link to a hosted demo (e.g., Render, Railway, or Heroku)._

---

## ⚙️ Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Backend    | Python, Flask       |
| Database   | SQLite              |
| Auth       | Flask-Login         |
| Frontend   | HTML, CSS, Bootstrap |
| Container  | Docker, Docker Compose |
| Email      | Flask-Mail + SMTP  |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
incident-management/
├── app/
│   ├── __init__.py          # App factory
│   ├── models.py            # DB models
│   ├── routes.py            # Main routes
│   ├── auth.py              # Authentication logic
│   ├── email_utils.py       # Email notifications
│   ├── templates/           # HTML templates
│   └── static/              # CSS styles
├── config.py                # App configuration
├── .env                     # SMTP & secret keys
├── run.py                   # App entry point
├── Dockerfile               # Docker container definition
├── docker-compose.yml       # Dev environment
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```
</details>

---

## 🛠️ Installation & Setup

### Option 1: 🐳 Docker (Recommended)

```bash
git clone https://github.com/yourusername/incident-management.git
cd incident-management

# Set environment variables
cp .env.example .env
nano .env

# Build and run the container
docker-compose up --build
```

Visit: [http://localhost:5000](http://localhost:5000)

---

### Option 2: ⚙️ Local Python Setup

```bash
git clone https://github.com/yourusername/incident-management.git
cd incident-management

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
nano .env

python run.py
```

---

## 🔐 Roles & Permissions

| Role     | Permissions                          |
|----------|---------------------------------------|
| Admin    | Full access (create/assign/resolve)   |
| Engineer | Update status, resolve, assign        |
| Reporter | Create and view their own incidents   |

---

## 📮 REST API Endpoints

| Method | Endpoint             | Description                |
|--------|----------------------|----------------------------|
| GET    | `/dashboard`         | View all incidents         |
| GET    | `/incident/new`      | Create incident form       |
| POST   | `/incident/new`      | Submit new incident        |
| GET    | `/incident/<id>`     | View or update incident    |
| POST   | `/incident/<id>`     | Update/assign/resolve      |

> Future improvement: `/api/incidents` with token authentication for external integrations.

---

## ✉️ Email Notification

- On new incident creation
- On incident update (status/assignment)

Emails are sent using `Flask-Mail` and Gmail SMTP.
Make sure to:
- Enable "Less Secure Apps" or
- Use an **App Password**

---

## 🧪 Sample Data

Create an admin user in SQLite after first run:

```bash
sqlite3 incidents.db
```

Then, use this Python snippet to hash password:

```python
from werkzeug.security import generate_password_hash
print(generate_password_hash('admin123'))
```

Insert into database:

```sql
INSERT INTO user (id, username, password, role)
VALUES (1, 'admin', '<hashed_password>', 'admin');
```

---

## 🖼️ Screenshots

> Add images to `/screenshots/` and link below.

- 🟦 Login Page  
- 🟨 Dashboard View  
- 🟩 Create & Edit Incident  

---

## 🔮 Roadmap

- [ ] User registration & password reset
- [ ] Audit log / activity history
- [ ] REST API docs (Swagger/OpenAPI)
- [ ] Search & filtering
- [ ] Export incidents (CSV)
- [ ] Unit and integration tests
- [ ] CI/CD pipeline (GitHub Actions)

---

## 🤝 Contributing

We welcome contributions!

1. 🍴 Fork the repository  
2. 🔧 Create your feature branch  
3. ✅ Test your changes  
4. 📩 Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Maintainer

**Madhukar Sammeta**  
DevOps Engineer 
[GitHub](https://github.com/iammadhukar177) | [LinkedIn](https://linkedin.com/in/madhukarsammeta)
