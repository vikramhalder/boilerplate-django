# Django Boilerplate Code

### #Install & configuration

##### 1. Create virtual env
```
$ py -m venv virtual-env
$ source virtual-env/bin/activate
or
$ source virtual-env/Scripts/activate
```
##### 2. Clone repositories
```
(virtual-env)$ git clone https://github.com/vikramhalder/django-boilerplate.git
```
##### 3. Install requirements.txt 
```
(virtual-env)$ cd django-boilerplate
(virtual-env)$ pip install -r requirements.txt 
```

##### 4. Change setting.py database configuration
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "django",
        'USER': "root",
        'PASSWORD': "",
        'HOST': "localhost",
        'PORT': 3306,
    }
}
```

##### 5. Deploy database 
```
(virtual-env)$ python manage.py makemigrations
(virtual-env)$ python manage.py migrate
```

##### 6. Run
```
(virtual-env)$ python manage.py runserver 
(virtual-env)$ python manage.py runserver 8080
(virtual-env)$ python manage.py runserver 0.0.0.0:8080
```
##### 7. Browse  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
