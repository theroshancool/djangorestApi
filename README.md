"# restapi" 

**📊 Employee and Department Management API**
This is a simple Django REST Framework based project created as part of my personal learning journey. It provides RESTful API endpoints for managing Departments, Employees, and file uploads in a company system.


**🚀 Features**
✅ Create, Read, Update, Delete (CRUD) operations for Departments

✅ CRUD operations for Employees

✅ Upload files to the server

✅ JSON-based communication using Django REST Framework

✅ Function-based API views with CSRF exemption for API endpoints


**/your_project/**
├── /EmployeeApp
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── DjangoApi/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py

**
Method | Endpoint | Description**
GET | /api/department/ | Get all departments
POST | /api/department/ | Add a new department
PUT | /api/department/ | Update a department (with ID)
DELETE | /api/department/{id}/ | Delete a department by ID
GET | /api/employee/ | Get all employees
POST | /api/employee/ | Add a new employee
PUT | /api/employee/ | Update an employee (with ID)
DELETE | /api/employee/{id}/ | Delete an employee by ID
POST | /api/SaveFile/ | Upload a file

📚 **Technologies Used**
Python 3

Django

Django REST Framework

SQLite (default Django database)

Postman (for API testing)

**📖 Purpose
This project was developed for learning and practicing Django REST Framework concepts including:**

API design

JSON parsing and serialization

File upload handling

CRUD operations via REST API
**
Understanding DRF serializers and views**

📌 Future Improvements
✅ Use Class-Based Views or ViewSets

✅ Add authentication (JWT/Token-based)

✅ Improve error handling and validation

✅ Add pagination and filtering

✅ Create a frontend or API documentation

