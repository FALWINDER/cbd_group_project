# cbd_group_project

A Django-based web project using MySQL as the backend database.

## Setup Instructions

### 1. Create Virtual Environment

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install django
pip install mysqlclient
```

Or, if you have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Configure the Database

Make sure your `settings.py` file includes the correct MySQL configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

### 6. Start the Development Server

```bash
python manage.py runserver
```

Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Notes

- To deactivate the virtual environment:
```bash
deactivate
```

- Always activate your virtual environment before working:
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

