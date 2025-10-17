
# Project Task Tracker

A Django REST Framework backend for managing projects and tasks.  
This app lets you create, update, and track projects and their tasks, with smart APIs for summaries, dashboards, and filtered searching.

---

## Features

- Create, view, update, and delete projects and tasks
- View summary of tasks (total, completed, pending) under each project
- Dashboard endpoint showing the count in each task status, overdue, and upcoming tasks
- Filter tasks by project name and status
- Pagination on task lists
- RESTful API built using Django and Django REST Framework

---

## Requirements

- Python 3.8+
- Django 3.2+
- djangorestframework

---

## Setup Instructions

1. **Clone the Repository**
git clone https://github.com/yourusername/project-task-tracker.git
cd project-task-tracker

2. **Create a Virtual Environment**
python -m venv env
- Windows: `env\Scripts\activate`
- Mac/Linux: `source env/bin/activate`

3. **Install Dependencies**
pip install django djangorestframework

4. **Apply Migrations**
python manage.py makemigrations
python manage.py migrate

5. **Run the Server**
python manage.py runserver

- Visit: [http://127.0.0.1:8000/api/projects](http://127.0.0.1:8000/api/projects)

---

## API Usage Examples

- List Projects:
GET /api/projects

- Create Project:
POST /api/projects

(JSON body required)

- Get Project Summary:
GET /api/projects/<id>/summary/

- List Tasks:
GET /api/tasks

- Filter Tasks:
GET /api/tasks?project=ProjectName&status=todo

- Dashboard:
GET /api/projects/<id>/dashboard/

## Directory Structure

project-task-tracker/
├── manage.py
├── db.sqlite3
├── tasktracker/
│ └── settings.py, urls.py, ...
├── tracker/
│ └── models.py, views.py, serializers.py, urls.py, ...

## Notes

- Default database: SQLite (`db.sqlite3`)
- To exclude database and environment files from Git, use a `.gitignore` file:
*.pyc
pycache/
db.sqlite3
env/
*.sqlite3

