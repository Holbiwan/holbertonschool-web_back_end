# Basic authentication📌

![Rest Api basic authentication](https://zupimages.net/up/24/25/wx7v.png)

### Topics covered in this Repository 🚀

* What authentication means
* What Base64 is
* How to encode a string in Base64
* What Basic authentication means
* How to send the Authorization header

# Implement a Basic Authentication on a simple API.

Guide which facilitates operations on the `User` model via an HTTP interface.

## Overview

The Simple API is structured into models and views, allowing for scalable management of user data and interactions.

## Models

Located in `models/`, these are foundational to the API's data handling:

- **`base.py`**: Core functionalities, including serialization.
- **`user.py`**: Definition and operations related to the User model.

## API

Served from `api/v1/`, the endpoints are organized as follows:

- **`app.py`**: API's main entry point.
- **`views/`**: Contains sub-modules for different aspects of the API.
- **`index.py`**: General endpoints like `/status` and `/stats`.
- **`users.py`**: Endpoints specifically for user management.

## Setup

First, ensure you have Python 3 and pip installed. Then, install the required dependencies:

```
pip3 install -r requirements.txt
```


Running the API
To launch the API, use the following command:
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

## API Endpoints

### Status Check

- `GET /api/v1/status`: Checks and returns the API's current status.

### Statistics

- `GET /api/v1/stats`: Provides statistical data of the API.

### User Management

- `GET /api/v1/users`: Fetches a list of all users.
- `GET /api/v1/users/:id`: Retrieves details of a specific user by ID.
- `POST /api/v1/users`: Adds a new user. Requires JSON input with fields `email`, `password`, and optionally `last_name` and `first_name`.
- `PUT /api/v1/users/:id`: Updates user data based on the user ID. Required JSON input: `last_name` and `first_name`.
- `DELETE /api/v1/users/:id`: Removes a user by ID.
  
### Author
**Sabrina PAPEAU** - [Github](https://github.com/Holbiwan)
