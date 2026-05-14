# 📝 Blogging Platform using Flask

This project is a full-stack blogging application built using the **Flask** web framework. The primary objective is to provide a platform where users can securely register, log in, create rich-text blog posts, and manage their content through a personalized dashboard.

## 🛠️ Initial Setup
- Initialized a dedicated virtual environment (`.venv`) for dependency management.
- Installed essential Flask extensions including Flask-SQLAlchemy and Flask-Bcrypt.
- Established the foundational project directory structure following industry best practices.

---

# 📅 Week 1: Foundation & Database Architecture

During this phase, the focus was on establishing a scalable project architecture and setting up the data persistence layer.

### 🏗️ Project Architecture (Blueprints)
- Organized the application using the **Blueprint** pattern to ensure modularity as the project grows.
- Created the `flaskblog/` package containing:
  - `__init__.py`: Handles app initialization and extension configuration.
  - `routes.py`: Manages all web traffic and URL routing logic.
  - `models.py`: Defines the database structure using classes.
- Maintained a clean `app.py` as the main entry point for the server.

### 📊 Database Configuration
- Integrated **SQLAlchemy ORM** for efficient database management.
- Designed two core data models:
  - **User**: Stores unique usernames, emails, and securely hashed passwords.
  - **Post**: Stores blog content with a relationship back to the author.
- Successfully generated the `site.db` SQLite file within the `/instance` directory.

---

# 📅 Week 2: User Authentication & Security

Phase two focused on transitioning from static pages to a dynamic platform with a secure user authentication system.

### 🔐 User Authentication & Security
* **User Sessions:** Integrated **Flask-Login** to manage secure user sessions, allowing for persistent login states across the site.
* **Password Hashing:** Implemented **Flask-Bcrypt** to ensure all user passwords are encrypted before being stored.

### 🗄️ Relational Database Management
* **Relational Schema:** Established an association between users and their content using a **One-to-Many relationship**.
* **Dynamic Profiles:** Configured the User model to support custom profile information and unique identifiers.

### 📝 Forms & Templates
* **Validation:** Used **Flask-WTF** to create registration and login forms with built-in CSRF protection and real-time data validation.
* **Master Layout:** Developed a master `layout.html` to provide consistent navigation that updates dynamically based on the user's login status.

---

# 📅 Week 3: Post CRUD & Tagging System

This phase transformed the application into a functional Content Management System (CMS).

### ✍️ Full CRUD Functionality
* **Post Management:** Developed backend routes allowing users to **Create, Read, Update, and Delete** their own blog entries.
* **Security:** Applied `@login_required` decorators to protect administrative routes from unauthorized access.

### 🏷️ Advanced Tagging & Editing
* **Many-to-Many Tags:** Implemented an association table allowing posts to be categorized with multiple searchable tags.
* **Rich Text Integration:** Integrated **Flask-CKEditor**, giving users a professional "What You See Is What You Get" interface for writing posts.

---

# 📅 Week 4: Frontend, Displaying Posts & Navigation

The final phase focused on the frontend architecture and optimizing the user experience.

### 📰 Dynamic Content Rendering
* **Enhanced Home Feed:** Configured `home.html` to dynamically iterate through all database entries and display them as a list of blog posts.
* **Rich Text Rendering:** Implemented the `| safe` Jinja2 filter to correctly render formatted HTML content from the editor.

### 🔢 Scalable Pagination & Navigation
* **Pagination:** Added **SQLAlchemy pagination** to the home route to handle large volumes of content by limiting posts per page.
* **UI Controls:** Integrated "Next" and "Previous" page links for seamless navigation.

### 🎨 UI/UX Improvements
* **Delete Modals:** Integrated **Bootstrap Modals** to serve as a confirmation step before a user permanently deletes a post.
* **Sidebar Layout:** Added a professional sidebar to the main layout for additional site navigation and categories.

## 🛠️ How to Run
1. Activate environment: `.\.venv\Scripts\activate`
2. Run app: `python app.py`
3. Visit: `http://127.0.0.1:5000`

# 🚀 Week 5: Commenting System Implementation

## **Project Overview**
This week focused on transitioning the blogging platform into a social space by allowing users to interact with posts. This involved complex database relationships and multi-method routing.

## **Key Features Added**
*   **Relational Database Models**: Linked `User`, `Post`, and `Comment` tables using SQL Foreign Keys.
*   **Dynamic Comment Rendering**: Comments are now fetched and displayed automatically under each specific post.
*   **Submission Handling**: Users can post comments via a secure, CSRF-protected form.
*   **Permission Logic**: Implemented conditional rendering to show the comment box only to logged-in users.

## **Technical Challenges Overcome**
### **Database Schema Synchronization**
Faced `OperationalError` due to schema mismatches. Resolved this by recreating the database environment and ensured that the `post` route correctly initializes the `CommentForm` to prevent `UndefinedError`.

### **Route Optimization**
Updated the `/post/<post_id>` route to support both `GET` (viewing) and `POST` (submitting) methods, ensuring a seamless user flow through post-submission redirection.

---
*Developed as part of the Flask Blog Project - Week 5*

# 🌟 Week 6: Advanced Content Management & Search

In the sixth week of the internship, I focused on improving content discoverability and organization by implementing a tagging system and a robust search engine.

## 🛠️ Key Features Added
- **Tagging System:** Added the ability for authors to categorize their posts using multiple tags (e.g., Python, Tutorial, News).
- **Global Search:** Implemented a search bar in the navigation header that queries the database for matches in both post titles and body content.
- **Tag Filtering:** Created dedicated tag pages that display all posts associated with a specific keyword.
- **Interactive Sidebar:** Updated the UI sidebar to provide quick links to trending tags and the latest posts.

## 🔧 Technical Details
- **SQLAlchemy Relationships:** Utilized a helper table to manage the many-to-many relationship between the `Post` and `Tag` models.
- **Flask-WTF:** Expanded the `PostForm` to include a dedicated `tags` field with validation.
- **Jinja2 Logic:** Enhanced templates to dynamically render search results and handle empty query states gracefully.

# 🧪 Week 7: Testing & Deployment Preparation

This week focused on transitioning the application from a local development environment to a production-ready state. The primary goals were ensuring code reliability through automated testing and configuring the app for cloud hosting.

## 🛠️ Key Features & Technical Tasks

### 1. Automated Unit Testing
- **Framework:** Utilized Python's built-in `unittest` library to create a robust testing suite.
- **Test Isolation:** Configured an in-memory SQLite database (`sqlite://`) for tests. This ensures that the testing process does not modify the actual production or development data.
- **Coverage:** Implemented tests for core functionalities, including:
  - **User Registration:** Validating that new users are correctly hashed and stored.
  - **Authentication Logic:** Ensuring the login system correctly handles valid/invalid credentials and session management.

### 2. Production Environment Configuration
- **WSGI Servers:** 
  - Integrated **Gunicorn** as the primary web server for Linux-based production environments.
  - Configured **Waitress** for local production-grade testing on Windows to bypass `fcntl` compatibility issues.
- **Environment Variables:** Prepared the application to use dynamic port binding via `os.environ.get("PORT")`, allowing it to run on cloud platforms like Railway or Render.

### 3. Dependency Management
- **Requirements File:** Generated a standardized `requirements.txt` using `pip freeze` to ensure all dependencies (Flask, SQLAlchemy, Bcrypt, etc.) are version-locked for deployment.
- **Procfile:** Created a `Procfile` to define the process type and the command for starting the web server in the cloud.

## 🚀 How to Run Tests
To run the automated test suite locally, use the following command:
```bash
python tests.py
