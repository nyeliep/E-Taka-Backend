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

To get LogicSpires-Backend up and running, follow these steps:

1. Clone this repository to your local machine:


   git clone https://github.com/akirachix/LogicSpires-Backend.git

2.Navigate to the project directory:

  cd LogicSpires-Backend

3.Install the Python dependencies:

  pip install -r requirements.txt

4.Set up the PostgreSQL database:

    Create a PostgreSQL database for LogicSpires.
    Configure the database connection in your Django settings.

5.Migrate the database:

  python manage.py migrate

6.Create a superuser account for admin access (if needed):

  python manage.py createsuperuser

7.Start the Django development server:

  python manage.py runserver

Your backend should now be running at http://localhost:8000.

