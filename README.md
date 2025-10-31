# SkillBoost Event - Django REST Framework Workshop

A comprehensive Django REST API project built for the SkillBoost event workshop, demonstrating best practices in building RESTful APIs with Django.

## 📋 Project Overview

This project is a complete implementation of a Django REST API for **Project and Task Management** featuring:

- User authentication with role-based access (JWT-based)
- CRUD operations for projects and tasks
- Task assignment and tracking
- Advanced filtering and pagination
- API documentation with Swagger/ReDoc

## 🚀 Features

- **User Management**: Registration, login, and role-based access control (Admin, Project Manager, Contributor)
- **Projects**: Create, read, update, and delete projects with ownership tracking
- **Tasks**: Manage tasks within projects with assignment capabilities
- **Authentication**: JWT token-based authentication
- **API Documentation**: Interactive API docs with Swagger UI
- **Search & Filter**: Advanced filtering and search capabilities
- **Pagination**: Efficient data pagination

## 🛠️ Technology Stack

- **Django**: 5.x
- **Django REST Framework**: 3.x
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: JWT (Simple JWT)
- **API Documentation**: drf-spectacular
- **Python**: 3.8+

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Setup Instructions

1. **Clone the repository**

   ```bash
   cd "git clone https://github.com/aachraf94/django-workshop.git"
   ```

2. **Create and activate virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/api/docs/
- **ReDoc**: http://127.0.0.1:8000/api/redoc/
- **OpenAPI Schema**: http://127.0.0.1:8000/api/schema/

## 🔑 API Endpoints

### Authentication

- `POST /api/register/` - User registration
- `POST /api/login/` - User login (get JWT tokens)
- `POST /api/token/` - Obtain JWT token pair
- `POST /api/token/refresh/` - Refresh access token

### Users

- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/{id}/` - Retrieve a specific user
- `PUT /api/users/{id}/` - Update a user
- `PATCH /api/users/{id}/` - Partially update a user
- `DELETE /api/users/{id}/` - Delete a user

### Projects

- `GET /api/projects/` - List all projects (with pagination)
- `POST /api/projects/` - Create a new project
- `GET /api/projects/{id}/` - Retrieve a specific project
- `PUT /api/projects/{id}/` - Update a project
- `PATCH /api/projects/{id}/` - Partially update a project
- `DELETE /api/projects/{id}/` - Delete a project

### Tasks

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT /api/tasks/{id}/` - Update a task
- `PATCH /api/tasks/{id}/` - Partially update a task
- `DELETE /api/tasks/{id}/` - Delete a task

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run with coverage:

```bash
coverage run --source='.' manage.py test
coverage report
```

## 📖 Workshop Learning Objectives

This project covers:

1. **Django Setup**: Project structure and configuration
2. **Models**: Creating database models with relationships (User, Project, Task)
3. **Serializers**: Data validation and transformation
4. **Views**: Function-based and class-based views (ViewSets)
5. **Authentication**: Implementing JWT authentication with role-based access
6. **Permissions**: Custom permissions and access control
7. **Task Assignment**: Managing user assignments and ownership
8. **API Documentation**: Auto-generating API docs with drf-spectacular
9. **Best Practices**: Code organization and DRY principles

## 📁 Project Structure

```
django_rest/
├── todo/                   # Main API app
│   ├── migrations/
│   ├── models.py          # Database models (User, Project, Task)
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views (ViewSets)
│   └── urls.py            # API routes
├── django_rest/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## 🎭 User Roles

The system supports three user roles:

- **ADMIN**: Full access to all resources
- **PROJECT_MANAGER**: Can manage projects and assign tasks
- **CONTRIBUTOR**: Can view projects and work on assigned tasks

## 🔧 Configuration

Key settings in `settings.py`:

- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Configure for production
- **DATABASES**: Update for production database
- **AUTH_USER_MODEL**: Custom User model with role-based access
- **CORS**: Enable CORS if needed for frontend

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL database
4. Set up static files serving
5. Use environment variables for secrets
6. Configure proper authentication and permissions

## 📝 License

This project is created for educational purposes as part of the SkillBoost event workshop.

## 👥 Contributing

This is a workshop project. Feel free to fork and extend it for your learning!

## 📧 Contact

For questions about this workshop project, please reach out during the SkillBoost event.

---

**Happy Coding! 🎉**
