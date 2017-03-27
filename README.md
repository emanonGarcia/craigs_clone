# Craigslist Clone

This is a simple clone of Craigslist using Django, and Bootstraps. Though on a much smaller scale this application showcases the core functionality of the full scale the American classified advertisements website.


### Prerequisites

Python3

```
pip install python3
```

Additional python libraries need to run this project

```
pip install -r requirements.txt
```


### Installing

After cloning or downloading this repo, change the settings.py to satisfy your personal specs:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<[your database name]>',
        'USER': '<[your username]>',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

From /mysite/craigslist execute:

```
python manage.py migrate
```

Then execute:

```
python manage.py runserver
```

and navigate to [Home Page](http://localhost:8000/craigslist/)


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootsrap](http://getbootstrap.com/) - Front-end web framework for designing websites
* [PostgreSQL](https://www.postgresql.org/download/) - An open source object-relational database system
* [Postico](https://eggerapps.at/postico/) - A Modern PostgreSQL Client for OSX


## Authors

* **Luis Garcia** - *Initial work* - [emanonGarcia](https://github.com/emanongarcia)
