# 🚨 Alert Guardian Backend

A real-world backend system that intelligently detects critical failures in travel (flight cancellations, hotel overbookings, blocked routes), raises alerts, and automatically escalates them if not resolved — all while managing user roles, logging actions, and providing real-time updates.

---

## 🌍 Project Summary

**Alert Guardian** is a domain-agnostic, production-grade backend system that simulates how modern systems handle emergency failures — but in a travel setting.

It:
- Detects disruptions in travel (e.g., canceled flights, unavailable hotels)
- Raises alerts for travel agents to act upon
- If an alert is not acknowledged in time, escalates it to the next available agent or suggests fallback actions
- Notifies users in real-time through WebSocket
- Logs all actions with timestamps for audits
- Uses modern backend tools like Celery, Airflow, Docker, PostgreSQL, and Redis


---

## 🔧 Technologies Used

| Category            | Tools & Libraries                                |
|---------------------|--------------------------------------------------|
| API Development     | FastAPI, Pydantic                                |
| Database ORM        | SQLModel (for standard CRUD)                     |
| Raw SQL Queries     | SQLAlchemy Core (for escalation logic, reports)  |
| Asynchronous Tasks  | Celery + Redis                                   |
| Real-Time Messaging | WebSocket (via FastAPI WebSocket routes)         |
| Scheduling          | Apache Airflow (for daily checks, retries)       |
| Authentication      | JWT + Role-Based Access Control (RBAC)           |
| Database            | PostgreSQL                                       |
| Containerization    | Docker, Docker Compose                           |
| Testing             | Pytest                                           |
| CI/CD (Optional)    | GitHub Actions / GitLab CI (optional integration)|

---

## 🧠 How the System Works

1. **Detection**: External services or users report a travel failure (e.g. flight canceled).
2. **Alert Creation**: An alert is created in the system with details.
3. **Acknowledge Window**: Assigned agent must acknowledge it within N seconds/minutes.
4. **Escalation**: If no response, system automatically escalates the alert.
5. **Fallback**: Suggests alternatives (e.g. nearby hotels, rebooking bus/train).
6. **Real-Time Updates**: Users see alert status changes live via WebSocket.
7. **Logging**: Every step is recorded for audit.

---

## 🧩 Core Features

### ✅ Alerts & Escalation
- Raise alert when disruption happens
- Assign to current on-duty agent
- If not acknowledged → escalate to next agent or trigger fallback
- Logged and trackable

### 🧑‍🤝‍🧑 User Management & Roles
- Customer → Can raise issues
- Travel Agent → Acknowledge alerts, manage fallbacks
- Admin → Manage users, view logs

### 🔒 Auth & RBAC
- Login with JWT
- Protect routes based on user role
- Travel agents and admins can’t self-register — only customers can

### 🔔 Real-Time WebSocket
- Sends updates to UI/dashboard when alert status changes
- Used for connected agent panels or monitoring views

### 🔁 Retry Logic
- Celery tasks retry escalation until acknowledged or max retries hit

### 🕓 Scheduled Jobs
- Airflow runs daily availability checks (e.g., hotel sync)
- Scheduled fallback prep (e.g., pre-caching alternate routes)

### 🧾 Audit Trail
- Who raised, acknowledged, or escalated alerts
- Stored in PostgreSQL `audit_logs` table
- Useful for compliance and reporting

---

## 🗂️ Folder Structure

```bash
project/
│
├── app/
│   ├── main.py              # FastAPI application instance
│   ├── models/              # SQLModel DB + Pydantic schemas
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── alert.py
│   │   ├── acknowledgement.py
│   │   └── shift.py
│   ├── api/                 # FastAPI route handlers
│   │   ├── users.py
│   │   ├── alerts.py
│   │   ├── auth.py
│   │   └── roles.py
│   ├── core/                # Auth logic, JWT, RBAC, WebSocket manager
│   ├── services/            # Business logic: escalation, fallback, user ops
│   │   ├── alert_service.py
│   │   ├── fallback_service.py
│   │   └── auth_service.py
│   ├── workers/             # Celery tasks
│   └── scheduler/           # Airflow DAGs
│
├── tests/                   # Pytest tests
├── docker/                  # Docker & Docker Compose setup
├── alembic/                 # DB migrations
└── requirements.txt         # Project dependencies
