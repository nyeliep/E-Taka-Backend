# LogicSpires-Backend

Welcome to the LogicSpires-Backend repository! This backend application powers the E-Taka project, an e-waste management platform dedicated to addressing the growing concern of electronic waste disposal and promoting recycling. Below, you'll find an overview and setup instructions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)



## Overview

E-Taka is an innovative e-waste management platform that aims to provide individuals with a convenient and eco-friendly way to dispose of their electronic waste while also offering a marketplace for buying and selling recyclable materials. This repository contains the backend code built with Django and PostgreSQL, responsible for managing user data, serving APIs, and handling various e-waste management tasks.

## Features

- User authentication and account management.
- Data retrieval for electronic waste disposal.
- Secure API endpoints for frontend integration.
- Integration with recycling companies for responsible disposal.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python and Django: Ensure you have Python and Django installed. You can find installation instructions at [python.org](https://www.python.org/) and [djangoproject.com](https://www.djangoproject.com/).
- PostgreSQL: Install and set up PostgreSQL as the database for this backend. You can find installation instructions at [postgresql.org](https://www.postgresql.org/).
- API Keys: Obtain API keys for location data and any external services you may use and configure them in your environment.

### Installation

### Step 1: Clone the repository
```sh
git clone https://github.com/akirachix/LogicSpires-Backend.git
```

### Step 2: Navigate to the project directory
```sh
cd LogicSpires-Backend
```

### Step 3: Activate Virtual environment
```sh
python3 -m venv env
```

### Step 4: Install the Python dependencies
```sh
pip install -r requirements.txt
```

### Step 5: Migrate the database
```sh
python manage.py migrate
```

### Step 6: Create a superuser account for admin access (if needed)
```sh
python manage.py createsuperuser
```

### Step 7: Start the Django development server
```sh
python manage.py runserver
```


Your backend should now be running at http://localhost:8000.

