# E-Commerce Order Management System

## Overview
This backend system manages and processes orders in an e-commerce platform. It provides:  
- **RESTful APIs** for order management and metrics reporting.  
- **Asynchronous order processing** using Celery and Redis.  
- **Database storage** using PostgreSQL.  
- **Metrics API** to track total orders, average processing time, and order statuses.  

---

## Setup Instructions

### 1️. Clone the Repository
```sh
git clone <YOUR_GITHUB_REPO_URL>
cd ecommerce
```

### 2. Setup Python (Python 3.13.2)
To install Python 3.13.2, use **pyenv**, a popular version manager for Python.

#### **🔹 Steps to Install Python Using pyenv**
1. Install **pyenv** by following the official guide:  
   👉 [pyenv GitHub Repository](https://github.com/pyenv/pyenv)
   
2. Install Python **3.13.2** using pyenv:
   ```sh
   pyenv install 3.13.2

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Start PostgreSQL & Redis
If you're working on locally
```sh
sudo service postgresql start
psql -U postgres -c "CREATE DATABASE ecommerce_db;"
sudo service redis-server start
```
If you want to run postgres using docker
```sh
docker run --name postgres_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=ecommerce_db -p 5432:5432 -d postgres:15
```

### 5. Run Database Migrations and Start Django Server
```sh
python manage.py migrate
python manage.py runserver
```

### 6. Start Celery Worker
```sh
celery -A ecommerce worker --loglevel=info
```

### 6. Run tests
```sh
DJANGO_SETTINGS_MODULE=ecommerce.test_settings pytest
```

# API Examples

---

## **1. Create an Order**
### **Request**
```sh
curl --location 'http://localhost:8000/orders/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=uFCD1rFNLPZrxF5pbPUI5b5q7WMDsg5f' \
--data '{
    "user_id": 101,
    "order_id": 670111,
    "item_ids": [1, 2, 3],
    "total_amount": 678.99
}'
```

### **Response**
```json
{"message":"Order received","order_id":"670111"}
```

## **2. View an Order**
### **Request**
```sh
curl --location 'http://localhost:8000/orders/670111'
```

### **Response**
```json
{"message":"Order received","order_id":"670111"}
```

## **3. Fetch key metrics**
### **Request**
```sh
curl --location 'http://localhost:8000/orders/metrics'
```

### **Response**
```json
{
    "total_orders": 10,
    "avg_processing_time": 0.042058,
    "order_status_counts": [
        {
            "status": "Pending",
            "count": 4
        },
        {
            "status": "Completed",
            "count": 6
        }
    ]
}
```
