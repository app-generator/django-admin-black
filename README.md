# [Django Admin Black](https://github.com/app-generator/django-admin-black)

Modern template for **Django Admin Interface** coded on top of **Black Dashboard**, an open-source `Boostrap 4` design from `Creative-Tim`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br />

> UI Kit: https://github.com/app-generator/ct-black-dashboard

<br />

**Links & Resources**

- [Django Black Dashboard](https://appseed.us/product/black-dashboard/django/) - free starter with the same design
- [Django Black Dashboard](https://django-black-dashboard.appseed-srv1.com/) - LIVE Demo

<br />

## Why `Django Admin Black`

- Modern `Bootstrap 4` Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

<br>

![Django Admin Black - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/196730732-dda1794b-93ce-48cb-bc5c-182411495512.png)

<br>

## How to use it

<br />

> Install the package via `PIP` 

```bash
$ pip install django-admin-black
// OR
$ pip install git+https://github.com/app-generator/django-admin-black.git
```

<br />

* Add 'admin_black' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

```python
    INSTALLED_APPS = (
        ...
        'admin_black.apps.AdminBlackConfig',
        'django.contrib.admin',
    )
```

<br />

> Create database tables

```bash
$ python manage.py migrate admin_black
$ # OR
$ python manage.py syncdb
```

<br />

> Collect static if you are in production environment:

```bash
$ python manage.py collectstatic
```

<br />

## Screenshots

> **Black Theme** - `Admin Section`  

![image](https://user-images.githubusercontent.com/51070104/196731580-f0766235-3c92-4d79-bc38-3c34ad511bdb.png)

<br />

> **Black Theme** - `Admin Widgets`  

![image](https://user-images.githubusercontent.com/51070104/196731649-dfa68903-2d3d-4a66-a169-6b88eb0326d1.png)

<br />

---
**[Django Admin Black](https://github.com/app-generator/django-admin-black)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
