# Kaizntree Backend Challenge

## Description

This project is a web application designed to manage inventory items. The project utilizes Django REST Framework for the backend with a PostgreSQL database, and includes Swagger for API documentation and Figma for frontend design mockups. The project is done as part of kaizntree backend challenge.
  
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

Note: Select the "pgAgent for PostgreSQL" during PostgreSQL installation as shown in the image below:

![Alt text](pgAgent.png?raw=true "PgAgent")

4. **Django Installation**:

   ```
   pip install django
   ```
5. **Django REST Framework Installation**:

  ```
   pip install djangorestframework
  ```
***Note: Make sure that you are using the same Python interpreter and virtual environment that you are using for your Django project.***
  
6. **Additional Packages Installation that project needs**:
The django-cors-headers package is for handling Cross-Origin Resource Sharing (CORS), and psycopg2-binary is a PostgreSQL adapter for Python.

   ```
   pip install django-cors-headers
   pip install psycopg2-binary
   ```
7. **Required Python Packages Installation**

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

8. **Creating mytestdb using PostgreSQL**:

   Note: You will have to launch pgAdmin4 application and create database named `mytestdb` in Databases as shown in image below:
   
   ![Alt text](mytestdb.png?raw=true "mytestdb")

9. **Setup the Migrations using given commands**:

   ```
   python manage.py makemigrations DashboardApp
   python manage.py migrate DashboardApp
   python manage.py makemigrations AccountApp
   python manage.py migrate AccountApp
   python manage.py migrate
   ```
10. **Running the Application**:

Note: In file kaizntree_be_challenge-main/kaizntree_be_challenge/settings.py change the "PASSWORD" field value on line 99 to your local Postgre SQL password set during PostgreSQL installation as shown in the image below

![Alt text](PasswordRequirement.png?raw=true "PasswordRequirement")

In the same file kaizntree_be_challenge-main/kaizntree_be_challenge/settings.py add your `UI domain` value as a string in the `CORS_ALLOWED_ORIGINS` field section on line 55-56 as shown in the image below

![Alt text](CORS.png?raw=true "CORS")

The environment variables like SECRET_KEY, DEBUG..etc are provided in `.env` file.

To run the application, navigate to the project directory in your terminal and execute:

   ```
   python manage.py runserver
   ```
This will start the Django development server, and you should be able to access the application at http://127.0.0.1:8000/.

11. **API Documentation**

The API endpoints are documented using Swagger. You can access the interactive endpoints documentation for the project at: [Swagger Editor Website](https://editor.swagger.io/)
You will have to copy the entire contents of openapi.yaml file from the project directory and paste it in Swagger editor to get interactive API documentation

12. **Frontend Mockups**
    
The frontend design mockups are available on Figma at the following link: [Figma Design Link](https://www.figma.com/file/fjzPIi67Jk7WgW3gjeA0Tk/Kaizntree-Full-Stack-Interview-UI-Template?type=whiteboard&node-id=0-1&t=T12L5wu2aGemt1Lk-0)

13. **Unit testind the Application**:
To test the API endpoints of the application use below commands

   ```
   python manage.py test DashboardApp
  python manage.py test AccountApp
   ```

14. **Why PostgreSQL?**
I chose PostgreSQL for its ability to handle complex data relationships and queries, crucial for the dashboard's interconnected data. Its ACID compliance ensures data integrity, while scalability and community support make it ideal for both development and production.

15. **Why React Frontend Framework?**
I chose React for its component-based architecture, enabling reusable UI elements and scalability. Its virtual DOM optimizes performance, and the extensive ecosystem supports rapid development. The large community provides ample resources and support.
   
16. **Why Github Pages to deploy Frontend?**
I opted for GitHub Pages for its simplicity and cost-effectiveness in hosting static sites, perfect for a React app. It offers seamless integration with GitHub for easy updates and leverages GitHub's infrastructure for reliability and quick setup.

17. **Why JWT for Authentication?**
JWT tokens are valued for its compact, self-contained format that speeds up authentication and reduces database queries. Its stateless nature aids in scaling, and digital signatures offer security, making it a top choice for secure and efficient authentication.

18. **Frontend URL?**
    
[Frontend Website](https://rukhsarrkhan.github.io/kaizntree_be_challenge_fe/)

19. **On Logout**

Refresh tokens are invalidated, so that no new access_token can be made with it but access token invalidates at its expiry time

In the context of using Django REST Framework with the djangorestframework-simplejwt package for JWT (JSON Web Token) authentication, access tokens are typically short-lived and are not stored server-side. Therefore, we cannot invalidate an access token in the same way we can blacklist a refresh token, which can be stored and checked against a list of blacklisted tokens.
