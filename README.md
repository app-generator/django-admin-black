# Django Admin Black

**Modern template for Django admin interface** coded in **Django Framework** by **AppSeed** [Web App Generator](https://appseed.us/app-generator)

<br>

## Why Django Admin Black?

- UI Kit: **[Black Dashboard](https://www.creative-tim.com/product/black-dashboard?AFFILIATE=128200)** (Free version) provided by **Creative-Tim**
- New fresh look
- Responsive mobile interface
- Useful admin home page
- Minimal template overriding
- Support RTL and LTR template
- Easy integration

<br />

## Screenshots

![Django Admin Black - Template project provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-dashboard-black/master/media/django-dashboard-black-screen.png)

<br>

## Installation

```bash
$ pip install git+https://github.com/app-generator/django-admin-black.git
$ # or
$ easy_install git+https://github.com/app-generator/django-admin-black.git
```

* Add 'admin_black' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

```python
    INSTALLED_APPS = (
        ...
        'admin_black.apps.AdminBlackConfig',
        'django.contrib.admin',
    )
```


* All programs you add in **INSTALLED_APPS** should look like this: **APP_NAME.apps.APP_NAMEConfig**.

> In this feature, we considered that each App can have its own icon, so we ask users to use this feature according to the method. Also in apps.py of each program according to the example add the icon field in the corresponding class. You can go **[here](https://django-dashboard-black.appseed.us/ui-icons.html)** to use more icons


```python

    from django.apps import AppConfig

    class APP_NAMEConfig(AppConfig):
        name = 'APP_NAME'
        icon = 'ICON_CLASS'  # for example: icon = 'tim-icons icon-atom'
```

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+ way):

```python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]
```

:warning: **Warning!!**
* Before Django 1.8 you should specify context processors different way. Also use ``django.core.context_processors.request`` instead of ``django.template.context_processors.request``.

```python
    from django.conf import global_settings

    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    )
```

* Create database tables:

```bash
$ python manage.py migrate admin_black
$ # or
$ python manage.py syncdb
```

* Collect static if you are in production environment:

```bash
$ python manage.py collectstatic
```

* Clear your browser cache

<br />

## More Details

### [Django Admin Black](https://github.com/app-generator/django-admin-black)

Start fast your next Django project by using functional django admin dashboard.

### [Black Dashboard](https://www.creative-tim.com/product/black-dashboard?AFFILIATE=128200)

**[Black Dashboard](https://www.creative-tim.com/product/black-dashboard?AFFILIATE=128200)** is a beautiful Bootstrap 4 Admin Dashboard with a huge number of components built to fit together and look amazing. If you are looking for a tool to manage and visualize data about your business, this dashboard is the thing for you. It combines colors that are easy on the eye, spacious cards, beautiful typography, and graphics.

<br />

---
**Django Admin Black** - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).