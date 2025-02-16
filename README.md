# Flint - AI-Powered Product Review Platform

## 🚀 Overview

Flint is an AI-powered product review platform where users can write and share reviews for any product they have purchased—whether online or offline. The platform categorizes products, verifies users, and enhances reviews using AI-driven insights to provide trusted product knowledge.

## 🔥 Features

-   **User Authentication**: Secure login/signup with email verification.
-   **Verified Users**: Users can be verified and will have a verification badge.
-   **Product Listings**: Products are stored in a categorized database.
-   **Review System**: Users can write reviews for specific products.
-   **AI-Enhanced Reviews**: Integration of GPT-4 to enhance and summarize user reviews.
-   **Clean & Modern UI**: Minimalist and glass-like user interface.

## 🛠️ Tech Stack

-   **Backend**: Django (Python)
-   **Database**: PostgreSQL
-   **Frontend**: Django Templates
-   **Authentication**: Django Authentication System
-   **AI Integration**: GPT-4 for enhanced review insights
-   **Deployment**: Docker, Gunicorn, Nginx

## 📌 Installation

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository

```sh
$ git clone https://github.com/your-username/flint.git
$ cd flint
```

### 2️⃣ Create a Virtual Environment

```sh
$ python3 -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3️⃣ Install Dependencies

```sh
$ pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```sh
$ python manage.py migrate
```

### 5️⃣ Run Development Server

```sh
$ python manage.py runserver
```

### 6️⃣ Create a Superuser (Admin Access)

```sh
$ python manage.py createsuperuser
```

## 🌟 Support

Give a ⭐️ to this repository if you liked our project!
