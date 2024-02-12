# Kaizntree Backend Challenge

## Description

This project is a web application designed to manage inventory items. The project utilizes Django REST Framework for the backend with a PostgreSQL database, and includes Swagger for API documentation and Figma for frontend design mockups. The project is done as part of kaizntree backend challenge.

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

API Documentation

The API endpoints are documented using Swagger. You can access the interactive endpoints documentation for the project at: [Swagger Editor Website](https://editor.swagger.io/)
You will have to copy the entire contents of openapi.yaml file from the project directory and paste it in Swagger editor to get interactive API documentation

The frontend design mockups are available on Figma at the following link:

[Figma Design Link](https://www.figma.com/file/fjzPIi67Jk7WgW3gjeA0Tk/Kaizntree-Full-Stack-Interview-UI-Template?type=whiteboard&node-id=0-1&t=T12L5wu2aGemt1Lk-0)

11. **Unit testind the Application**:
To test the API endpoints of the application use below commands

python manage.py test DashboardApp
python manage.py test AccountApp

13. **Why PostgreSQL?**
I chose PostgreSQL for this project primarily because it offers robust support for complex queries and relationships between data entities, which is essential for managing the interconnected data structure of the item dashboard. Its ACID compliance ensures reliable transaction processing, crucial for maintaining data integrity. Additionally, PostgreSQL's scalability and strong community support make it a reliable choice for both development and production environments, aligning well with the project's requirements for a secure, efficient, and scalable database solution.

14. **Why React Frontend Framework?**
I chose React for the front-end development of this project because of its flexibility, efficiency, and strong community support. React's component-based architecture allows for the development of reusable UI elements, making the codebase more manageable and scalable as the project grows. Its virtual DOM implementation ensures high performance and a smooth user experience, even for complex applications with dynamic data. Additionally, React's extensive ecosystem, including tools and libraries, facilitates rapid development and feature implementation. The widespread adoption of React also means there's a wealth of resources, tutorials, and community support available, which is invaluable for solving development challenges and staying up to date with best practices.
   
15. **Why Github Pages to deploy Frontend?**
I opted for GitHub Pages to deploy the React front-end of this project for several reasons. Firstly, it offers a straightforward and cost-effective solution for hosting static websites, which is ideal for a React application. GitHub Pages integrates seamlessly with the existing GitHub repository, simplifying the deployment process and making updates easy to manage directly from the version control system. This choice also leverages GitHub's robust infrastructure, ensuring high availability and reliability for the deployed application. Additionally, using GitHub Pages aligns with the project's need for a quick setup and minimal configuration, allowing me to focus more on development while still ensuring a professional, accessible presentation of the front-end.

16. **Why JWT for Authentication?**
JWT tokens are praised for their efficiency and security in web development. They are compact, allowing for fast transmission, and self-contained, carrying all necessary user data. This makes authentication processes efficient, as it reduces the need to query the database repeatedly. Additionally, their stateless nature simplifies scaling by eliminating server-side session storage. Security is another key advantage; JWTs can be digitally signed, ensuring data integrity and authenticating that the tokens are from a legitimate source. This combination of features makes JWT an excellent choice for secure, scalable, and efficient web application authentication.

17. **Frontend URL?**
    
[Frontend Website]([https://editor.swagger.io/](https://rukhsarrkhan.github.io/kaizntree_be_challenge_fe/)https://rukhsarrkhan.github.io/kaizntree_be_challenge_fe/)

18. 
