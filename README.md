# Django Form


## Table of Contents

- Description
- Technologies
- How to Create


## Description

> It is an App in which we can fill the information of incident in which we uses Django for backend and PostgreSQL Database.


## Technologies

- Django
- Python
- Jinja2


## How To Create

### Set Up

Give following commands in command prompt

```html
    $ django-admin startproject markytics
    $ python mange.py start app form
    $ python manage.py runserver
```
and after that run at  `http://127.0.0.1:8000/`

After making the model put following command in cmd

```html
    $ python mange.py makemigrations
    $ python manage.py migrate
```


### Steps to write code

> Step 1: First add path of new app `form` in `urls.py`

> Step 2: Create model which is written in `form/models.py`

> Step 2: Register this model in `form/admin.py`

> Step 3: Then create file `forms.py` as `form/forms.py` and create form from existing model.

> Step 4: Create Api(function) in `views.py` file for creating form and manage the the `GET` and `POST` request and last render to the template `create_form.html` 

> Step 5: Add this Api to `urls.py` as `form/urls.py`

> Step 6: Create `create_form.html` file as `template/create_form.html` and write html, bootstrap, jinja2 code for frontend


[Back To The Top](#django-form)
