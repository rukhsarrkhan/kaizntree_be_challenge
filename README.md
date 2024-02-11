# Kaizntree Backend Challenge

## Description

This project is a web application designed to manage [briefly describe the core functionality of your app, e.g., "inventory", "customer relations", "content" etc.]. It provides an interface for users to [describe what users can do with your application]. The project utilizes Django REST Framework for the backend with a PostgreSQL database, and includes Swagger for API documentation and Figma for frontend design mockups.

## Features : TBD

- Inventory Management

  
## Installation

Follow these steps to set up the project environment and run the application:

1. **Python Installation**: Ensure that Python is installed on your system. If not, download and install it from the [official Python website](https://www.python.org/). During installation, check the option to "Add Python to PATH".

2. **Verify Python Installation**: You can verify the Python installation by running the following command in the terminal:

   ```sh
   python --version

This should output the version of Python installed.

Install PostgreSQL: Download and install PostgreSQL. Once installed, you can connect to the database using tools like pgAdmin.

Set PostgreSQL Password: Set up a password for the default PostgreSQL user (usually postgres).

Install Django:

  pip install django

Install Django REST Framework:

  pip install djangorestframework
  
Install Additional Packages: Install additional packages project needs. For example:

pip install django-cors-headers
pip install psycopg2-binary

The django-cors-headers package is for handling Cross-Origin Resource Sharing (CORS), and psycopg2-binary is a PostgreSQL adapter for Python.

Running the Application

To run the application, navigate to the project directory in your terminal and execute:

python manage.py runserver

This will start the Django development server, and you should be able to access the application at http://127.0.0.1:8000/.

API Documentation

The API endpoints are documented using Swagger. You can access the interactive documentation at:

Swagger API Documentation

Design Mockups : TBD

The frontend design mockups are available on Figma at the following link:

Figma Design Link : TBD

Why PostgreSQL?
PostgreSQL was chosen as the database for this project due to its robustness, scalability, and strong community support. It provides advanced features such as full ACID compliance, reliable transactional integrity, and support for complex queries and data types, which are essential for [explain any specific needs of your project].
