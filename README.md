
# Pathan Ecom

Pathan Ecom implements a robust multi-vendor e-commerce platform, enabling seamless online shopping experiences for both vendors and customers. Built upon the secure foundations of Django and PostgreSQL, it offers a feature-rich environment to manage products, orders, user accounts, and payments.



## Features
Key Features:

- **Multi-Vendor Support :** Enables multiple vendors to register, manage their stores, and sell products on the platform.
- **User Management :**  Provides user registration and login functionalities. Customers can browse products, add items to carts, place orders, and view their order history.
- **Category View :**  Organizes products into well-defined categories.
- **Search Functionality :** Allows users to search for products by name or relevant keywords.
- **Product Detail View :** Provides detailed information about each product, including images, descriptions, and pricing.
- **Cart Management:** Enables users to add, remove, and adjust quantities of products in their carts.
- **My Account Page :** Offers a dedicated dashboard for users to view order history and manage preferences.
- **Checkout :** Guides users through the checkout process, allowing them to enter shipping details and utilize a secure payment gateway for transactions.
- **Vendor Administration :** Empowers vendors with a dedicated admin interface to manage their stores, add/edit/delete products, view their order history, and track sales.
- **Payment Gateway Integration :** Integrates with SSLcommerz to securely process payments.
- **Deployment Ready :** Deployment on PythonAnywhere




#### Technologies:

- Backend: Django (Python web framework), Basic Tailwind CSS
- Database: PostgreSQL 
- Payment Gateway: SSLcommerz


## Installation

- Create a virtual environment:
 ``` bash 
 python -m venv venv
 ```
- Activate the virtual environment: 
```
source venv/scripts/activate 
```
- Install dependencies: 
```
pip install -r requirements.txt
```
- Migrate database tables: 
```
python manage.py makemigrations
python manage.py migrate
```
- Create a superuser account (for initial admin access):
``` 
python manage.py createsuperuser
```
- Run server:
```
 python manage.py runserver
 ```

 
    
## Screenshots

