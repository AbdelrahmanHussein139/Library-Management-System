# Library Management System (FastAPI + PostgreSQL + Docker)

A **Library Management System** built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **Alembic**, following **Domain-Driven Design (DDD)** principles.  
It allows managing books and members, borrowing and returning books, and includes pagination, search, and Docker support.

---

## Project Architecture

```
app/
├── domain/              # Business core (no FastAPI or DB logic)
├── application/          # Use cases and business services
├── infrastructure/       # Database (SQLAlchemy, Alembic) + config
├── interfaces/           # FastAPI routes (HTTP interface)
├── main.py               # FastAPI entry point
```

**Layers Overview**
- **Domain** — Entities and repository interfaces  
- **Application** — Use cases (BookService, MemberService)  
- **Infrastructure** — PostgreSQL, SQLAlchemy models/repositories  
- **Interfaces** — FastAPI routers (books, members)

---

## Requirements

- Python 3.10+
- PostgreSQL 15+
- Docker & Docker Compose (optional but recommended)

---

## Setup (Local Development)

### 1. Clone & enter the project
```bash
git clone <your-repo-url>
cd libraryManagementSystem
```

### 2. Create & activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# .\venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in your project root:
```env
POSTGRES_USER=libuser
POSTGRES_PASSWORD=abd123456
POSTGRES_DB=libdb
DATABASE_URL=postgresql+psycopg2://libuser:abd123456@localhost:5432/libdb
```

If using Docker Compose, change host to `db`:
```
DATABASE_URL=postgresql+psycopg2://libuser:abd123456@db:5432/libdb
```

### 5. Run Alembic migrations
```bash
alembic upgrade head
```

### 6. Start the FastAPI app
```bash
uvicorn app.main:app --reload
```

App runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Run with Docker Compose (Recommended)

### 1. Build and start the containers
```bash
docker compose build
docker compose up
```

### 2. Access the app
```
http://localhost:8000
```

### 3. PostgreSQL container info
- Container name: `db_container`
- Host port: `5433`
- Internal port: `5432`

### 4. Open PostgreSQL CLI inside container
```bash
docker exec -it db_container psql -U libuser -d libdb
```

---

## API Endpoints

### Books

| Method   | Endpoint                              | Description                                         |
| -------- | ------------------------------------- | --------------------------------------------------- |
| POST     | /books/                               | Add a new book                                      |
| GET      | /books/                               | List all books (supports `skip`, `limit`, `search`) |
| GET      | /books/{book_id}                      | Get details of a specific book                      |
| PUT      | /books/{book_id}                      | Update book info                                    |
| DELETE   | /books/{book_id}                      | Delete a book                                       |
| POST     | /books/borrow/{book_id}/{member_id}   | Borrow a book                                       |
| POST     | /books/return/{book_id}               | Return a borrowed book                              |

### Members

| Method   | Endpoint               | Description                                           |
| -------- | ---------------------- | ----------------------------------------------------- |
| POST     | /members/              | Add a new member                                      |
| GET      | /members/              | List all members (supports `skip`, `limit`, `search`) |
| GET      | /members/{member_id}   | Get member details                                    |
| PUT      | /members/{member_id}   | Update member info                                    |
| DELETE   | /members/{member_id}   | Delete a member                                       |

---

## Pagination & Search Examples

**Books**
```bash
# List first 5 books containing "code"
curl "http://127.0.0.1:8000/books/?skip=0&limit=5&search=code"
```

**Members**
```bash
# Get members with "ali" in their name or email
curl "http://127.0.0.1:8000/members/?skip=0&limit=10&search=ali"
```

---

## Example API Usage

### Create a Book
```bash
curl -X POST "http://127.0.0.1:8000/books/" \
-H "Content-Type: application/json" \
-d '{"title": "Clean Code", "author": "Robert C. Martin"}'
```

### Create a Member
```bash
curl -X POST "http://127.0.0.1:8000/members/" \
-H "Content-Type: application/json" \
-d '{"name": "Alice Johnson", "email": "alice@example.com"}'
```

### Borrow a Book
```bash
curl -X POST "http://127.0.0.1:8000/books/borrow/1/<member_uuid>"
```

### Return a Book
```bash
curl -X POST "http://127.0.0.1:8000/books/return/1"
```

### Delete a Member
```bash
curl -X DELETE "http://127.0.0.1:8000/members/<member_uuid>"
```

---

## Swagger & API Docs

FastAPI provides Swagger UI automatically.

Once running, open:
```
http://127.0.0.1:8000/docs
```

or Redoc:
```
http://127.0.0.1:8000/redoc
```

You can test endpoints directly in your browser — no external client needed.

---

## Database Migrations (Alembic)

Generate a new migration when models change:
```bash
alembic revision --autogenerate -m "update models"
```

Apply migrations:
```bash
alembic upgrade head
```

---

## Testing

Run unit or integration tests:
```bash
pytest -v
```

Make sure the test database URL is configured (e.g., SQLite or a separate test DB).

---

## Environment Variables Summary

| Variable            | Description                  | Example                                                 |
| ------------------- | ---------------------------- | ------------------------------------------------------- |
| POSTGRES_USER       | Database username            | libuser                                                 |
| POSTGRES_PASSWORD   | Database password            | abd123456                                               |
| POSTGRES_DB         | Database name                | libdb                                                   |
| DATABASE_URL        | SQLAlchemy connection string | postgresql+psycopg2://libuser:abd123456@db:5432/libdb   |

---

**Author:** Abdelrahman Hussein  
**Tech Stack:** FastAPI | SQLAlchemy | Alembic | PostgreSQL | Docker  
**Version:** 1.0.0
````
