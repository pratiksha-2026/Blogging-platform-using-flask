# Blogging Platform using Flask

This project is a full-stack blogging application built using the **Flask** web framework. The goal is to create a platform where users can register, log in, create posts, and manage their own content.

## Initial Setup
- Initialized virtual environment (`.venv`).
- Installed Flask and essential extensions like Flask-SQLAlchemy.
- Created basic project directory structure.

# Blogging Platform - Week 1: Foundation & Database

This repository contains the progress for **Week 1** of the Python Web Development internship. During this phase, the focus was on establishing a scalable project architecture and setting up the data persistence layer.

## 🚀 Accomplishments

### 🏗️ Project Architecture (Blueprints)
- Organized the application using the **Blueprint** pattern to move away from a single-file structure.
- Created the `flaskblog/` package containing:
  - `__init__.py`: For app initialization and extension configuration.
  - `routes.py`: To handle web traffic and URL routing.
  - `models.py`: To define the database structure.
- Maintained a clean `app.py` as the entry point for the server.

### 📊 Database Configuration
- Integrated **SQLAlchemy ORM** for database management.
- Designed two primary data models:
  - **User**: Stores usernames, emails, and hashed passwords.
  - **Post**: Stores blog content with a relationship to the User.
- Successfully generated the `site.db` SQLite file within the `/instance` directory.

### 🎨 Frontend & Styling
- Set up the `templates/` folder with an initial `index.html`.
- Added a `static/` folder with `main.css` for custom styling.

## 🛠️ How to Run
1. Activate the environment: `.\.venv\Scripts\activate`
2. Run the application: `python app.py`
3. View at: `http://127.0.0.1:5000`

## 📁 Project Structure
```text
├── flaskblog/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── instance/
│   └── site.db
├── app.py
└── README.md