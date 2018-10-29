# capstone
capstone project for MCS

# set up 
## create virtual environment
```python3 -m venv venv```

## start venv
```source venv/bin/activatee```

## install Django & Django-heroku & gunicorn & auth
```
pip install django==2.1
pip install django-heroku
pip install gunicorn
pip install social-auth-app-django
```

## install database and runserver
```
python manage.py migrate
python manage.py runserver
```
