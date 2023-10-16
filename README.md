# EduTrack

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Conclusion](#conclusion)

## Introduction


"EduTrack: Navigating Student Success."

Edutrack, is a web-based  student information system, designed to help educational institutions efficiently manage student information, including their marks, attendance, and fees. This README provides an overview of the system, how to set it up, and how to use it.

## Features
- Student Marks Management
- Student Fees Management
- Student Attendance Tracking
- User Authentication (based on Django's built-in User model)
- User-friendly interface
- Fine and examination fees tracking

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python (3.x) and pip installed
- Django web framework
- Required Python packages (specified in `requirements.txt`)
- docker-compose
- docker

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system

2. Install docker-compose:

   ```sh
   sudo apt-get update
   sudo apt-get install docker-compose-plugin

3. Install requirements:
   ```sh
   pip install -r requirements.txt
   
## Usage
Create and activate virtual environment:
   
  ```sh
  python3 -m venv env
  source env/bin/activate
  ```

### Run with Django

  ```sh
  python3 manage.py migrate
  python3 manage.py makemigrations
  python3 manage.py runserver
  ```

### Run with docker-compose

  ```sh
  sudo docker-compose down &&
  sudo docker-compose up
  ```

## Documentation

Students need to register using their personal information:
1. Enrollment number
2. First Name
3. Last Name
4. Email
5. Phone
6. Password

This data will be stored in the database using a predefined model 'User' that django readily offers.

![register](https://github.com/Arjun4522/EduTrack/assets/94633408/dd4738d4-7c5a-4c70-847f-0d2219f212bf)

SQLite has been used for the database engine. It is a lightweight, open-source, embedded relational databse management system.

![db](https://github.com/Arjun4522/EduTrack/assets/94633408/7b7e7c5a-2878-4c63-910e-bb713c3fa478)

Once registered, they can login using their registered information:
1. Enrollment Number
2. Password

![login](https://github.com/Arjun4522/EduTrack/assets/94633408/d78d76e0-de4a-4dc5-ac4a-9b645d9f5a55)

The web application has been built on the MVT, or the Model-View-Template architecture. 

The system comprises of the following relations:
1. Student Information
2. Student Marks
3. Student Fees
4. Student Attendance

All above models are linked to the `User` model(foreign key).

Each table(relation) has a 'model' that defines the schema/architecture of the table. The models are defined in the `models.py` file in the app directory. Each model has a view of it's own. A 'view' is the request handler of the particular model. It takes in the request as a parameter, processes the request, and renders the corresponding template. The `views.py` file in the app folder consists of the views. The 'templates' are the static contents of the application. The templates comprise of the whole frontend of the application.
The `app/templates` directory contain the template files. 


![mvt](https://github.com/Arjun4522/EduTrack/assets/94633408/bc70c596-56a2-4604-aba6-522abc7c5c5f)

Additional files include:
1. `urls.py`- routes/urls
2. `forms.py`- form structures
3. `admin.py`- model registration
4. `db.sqlite3`- SQL file

![info](https://github.com/Arjun4522/EduTrack/assets/94633408/30a54ac3-49e1-4cc7-a5b0-9c5ae993c12d)


![marks](https://github.com/Arjun4522/EduTrack/assets/94633408/d0e451fb-992a-4947-a705-a6f1a30d1b42)

Above images show the different tabs, `personal information` and `student marks`. The personal information data is being stored in the `User` model. Marks of each student will be input by the admin in the admin portal of the system. Django provides a built-in admin portal for ease of use. 

![backend](https://github.com/Arjun4522/EduTrack/assets/94633408/a5250b41-c3ac-4fef-8cc9-4521591e74cf)

Below is the logical view of the student marks table.

![db_marks](https://github.com/Arjun4522/EduTrack/assets/94633408/64f92e5d-a76d-4dad-a45a-cd9187d783d3)






   
