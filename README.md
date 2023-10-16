# EduTrack

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

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
 








   
