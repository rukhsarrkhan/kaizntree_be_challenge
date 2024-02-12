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
   ```
This should output the version of Python installed.

3. **PostgreSQL Installation**: Download and install PostgreSQL.You can use [official PostgreSQL website](https://www.postgresql.org/download/). Once installed, you can connect to the database using tools like pgAdmin.

Set PostgreSQL Password: Set up a password for the default PostgreSQL user (usually postgres).

4. **Install Django**:

   ```
   pip install django
   ```
5. **Install Django REST Framework**:

  ```
   pip install djangorestframework
  ```
***Note: Make sure that you are using the same Python interpreter and virtual environment that you are using for your Django project.***
  
6. **Install additional packages project needs. For example**:
The django-cors-headers package is for handling Cross-Origin Resource Sharing (CORS), and psycopg2-binary is a PostgreSQL adapter for Python.

   ```
   pip install django-cors-headers
   pip install psycopg2-binary
   ```
7. **Installing required python packages**

***Navigate to the project directory within the terminal and proceed***

‘environ’ module is used to configure your Django application with environment variables. Install it using this command:

   ```
   python -m pip install django-environ
   ```
Install the ‘rest_framework_simplejwt’ module, using this command in your terminal:

   ```
   python -m pip install djangorestframework-simplejwt
   ```
Check the list of installed modules by running:

   ```
   python -m pip list
   ```
You should see 'django-environ' and 'rest_framework_simplejwt' in the output. If not, you may need to activate your virtual environment first. You can do that by running:
`source venv/bin/activate` # for Linux or Mac and `venv\Scripts\activate` # for Windows
Replace ‘venv’ with the name of your virtual environment folder.

8. **Setup the Migrations using given commands**:

   ```
   python manage.py makemigrations DashboardApp
   python manage.py migrate DashboardApp
   python manage.py migrate AccountApp
   python manage.py makemigrations AccountApp
   python manage.py migrate
   ```
9. **Running the Application**:
Note: In file kaizntree_be_challenge-main/kaizntree_be_challenge/settings.py change the "PASSWORD" field value on line 97 to your local Postgre SQL password set during PostgreSQL installation as shown in the image below
![Alt text](PasswordRequirement.png?raw=true "PasswordRequirement")

To run the application, navigate to the project directory in your terminal and execute:

   ```
   python manage.py runserver
   ```
This will start the Django development server, and you should be able to access the application at http://127.0.0.1:8000/.

API Documentation

The API endpoints are documented using Swagger. You can access the interactive endpoints documentation for the project at: [Swagger Editor Website](https://editor.swagger.io/)
You will have to copy the entire contents of openapi.yaml file from the project directory and paste it in Swagger editor to get interactive API documentation

Design Mockups : TBD

The frontend design mockups are available on Figma at the following link:

Figma Design Link : TBD

Why PostgreSQL?
PostgreSQL was chosen as the database for this project due to its robustness, scalability, and strong community support. It provides advanced features such as full ACID compliance, reliable transactional integrity, and support for complex queries and data types, which are essential for [explain any specific needs of your project].
