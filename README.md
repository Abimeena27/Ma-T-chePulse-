# Ma TâchePulse

# TâchePulse Task Management Application

Master your tasks effortlessly with TâchePulse - your personal productivity pulse!

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Routes](#routes)
- [License](#license)

## Introduction
TâchePulse is a simple task management application designed to help you manage your tasks effortlessly. This application is built using Flask, HTML, and JavaScript.

## Features
- User authentication
- Task management (add, update, delete tasks)
- Responsive design

## Requirements
- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tachepulse.git
    cd tachepulse
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install Flask
    ```

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Folder Structure


tachepulse/
├── static/
│   ├── user.png
│   └── login.js
├── templates/
│   ├── index.html
│   └── login.html
├── app.py
└── README.md


## Routes

- `/` (GET): Renders the login page.
- `/login` (POST): Validates user credentials.
- `/dashboard.html` (GET): Renders the main task management page after successful login.

## License
This project is licensed under the MIT License.

