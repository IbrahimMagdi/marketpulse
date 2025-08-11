# MarketPulse

MarketPulse is a Django-based backend platform for real-time stock price monitoring, alert management, and user notifications. It leverages Django REST Framework for secure API endpoints, Celery for background tasks (like fetching stock data and checking alerts), and JWT Authentication for user management. The project is designed for extensibility and production deployment.

---

## 🚀 Features

- **User Authentication**  
  Secure registration and login using JWT tokens ([SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)).

- **Stock Price Monitoring**  
  Periodic fetching of stock prices from an external API using Celery workers and Redis as a broker.

- **User Alerts**  
  Users can create alerts for specific stocks with conditions (e.g. price above/below a value). Alerts are checked automatically and notifications are sent.

- **RESTful API**  
  Endpoints for authentication, stocks listing, alerts CRUD, and alert history.

- **Notifications**  
  Email notifications are sent to users when their alert conditions are met.

---

## 🗂️ Tech Stack

- Python, Django, Django REST Framework
- Celery + Redis (as broker and result backend)
- JWT Authentication (SimpleJWT)
- PostgreSQL
- AWS (for deployment)
- Postman (for API testing)

---

## 📦 Setup & Local Development

### 1. Clone the repository
```bash
git clone https://github.com/IbrahimMagdi/marketpulse.git
cd marketpulse
```

### 2. Create a virtual environment and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file or set the following variables as needed:

- `DEBUG` (e.g., True or False)
- `SECRET_KEY`
- `DB_ENGINE` (e.g., `django.db.backends.postgresql`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_USE_TLS`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `STOCK_API_KEY` (API key for stock data)
- `CELERY_BROKER_URL` (usually `redis://127.0.0.1:6379/0`)
- `CELERY_RESULT_BACKEND` (usually same as broker)

### 4. Migrate the database
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Start Celery worker and beat
```bash
celery -A core worker --loglevel=info
celery -A core beat --loglevel=info
```

---

## 🔌 API Endpoints

### **Home**
| Endpoint           | Method | Description        |
|--------------------|--------|-------------------|
| `""` | GET   | To view current stock prices     |

### **Authentication**
| Endpoint            | Method | Description        |
|---------------------|--------|-------------------|
| `/api/auth/sign-up` | POST   | Register user     |
| `/api/auth/sign-in` | POST   | Obtain JWT tokens |
| `/api/auth/token/refresh` | POST   | refresh JWT tokens |

### **Stocks**
| Endpoint             | Method | Auth | Description                    |
|----------------------|--------|------|--------------------------------|
| `/api/stocks/list`       | GET    | Yes  | List stocks and their prices   |
| `/api/stocks/details` | GET    | Yes  | details stocks and their prices   |

### **Alerts**
| Endpoint              | Method | Auth | Description                        |
|-----------------------|--------|------|------------------------------------|
| `/api/alerts/create`  | POST   | Yes  | Create alert                       |
| `/api/alerts/list`    | GET    | Yes  | List your alerts                   |
| `/api/alerts/details` | GET    | Yes  | details your alert                     |
| `/api/alerts/update`  | PUT    | Yes  | Update alert                       |
| `/api/alerts/delete`  | DELETE | Yes  | Delete alert                       |

### **Triggered**
| Endpoint              | Method | Auth | Description                        |
|-----------------------|--------|------|------------------------------------|
| `/api/triggered/list` | GET    | Yes  | List triggered (historical) alerts |

---

## ⚙️ Background Tasks

| Task                    | Description                       | Schedule (Default) |
|-------------------------|-----------------------------------|--------------------|
| `fetch_stock_prices`    | Fetch latest stock prices         | Every 5 minutes    |
| `check_alerts`          | Evaluate and trigger user alerts  | Every 5 minute     |

Scheduling is managed with **Celery Beat** (see `CELERY_BEAT_SCHEDULE` in settings).

---

## 📨 Notifications

- Email notifications are sent to users when alert conditions are met.
- Notification logic is in `send_alert_notification` (pluggable for SMS, push, etc).

---

## 🧪 API Testing

- Import the provided Postman collection [MarketPulse.postman_collection.json](./MarketPulse.postman_collection.json) in Postman to test all endpoints.
- The collection includes JWT authentication and sample requests for all main features.

---
## 🔄 Deployment Workflow

This project is integrated with an automated CI/CD workflow that triggers on every new release.  
Upon release, the latest code is automatically built, tested, and deployed to the production server without manual intervention.  
This ensures continuous delivery and quick updates to the live environment.
---
## 🌐 Live Demo / Server Access

You can try the app on the server via the following link:
http://13.62.72.179/
---
## 📁 Project Structure

```
├── README.md
├── backend
│   ├── __init__.py
│   ├── alerts
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── coding
│   │   │   ├── __init__.py
│   │   │   ├── api_views
│   │   │   └── services
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tasks.py
│   │   ├── templates
│   │   │   └── home.html
│   │   ├── tests.py
│   │   └── views.py
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── extension
│   ├── pagination.py
│   ├── regex_patterns.py
│   └── string.py
├── manage.py
├── marketpulse.postman_collection.json
├── requirements.txt
...
```


---

## ✉️ Contact

For questions or contributions, feel free to open an issue or contact [Ibrahim Magdi](mailto:ibrahimmagdi333@gmail.com).

---
