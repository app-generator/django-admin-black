# Django Admin Black

Modern template for **Django admin interface** coded on top of Black Dashboard (free version) from **Creative-Tim**

> Originally coded by [Iman Karimi](https://github.com/imankarimi), actively versioned and supported by [AppSeed](https://appseed.us/) via Github (issues tracker) and [Discord](https://discord.gg/fZC6hup) - 24/7 LIVE Service.

<br>

**Links & Resources**

- [Django Black Dashboard](https://appseed.us/admin-dashboards/django-dashboard-black) - Open-source starter that uses the same UI Kit
- [Django Black Dashboard - DEMO](https://django-dashboard-black.appseed.us/login/) - LIVE Deployment

<br />

## Why Django Admin Black?

- UI: **[Black Dashboard](https://bit.ly/2L0W6Z7)** v1.0.1 provided by *Creative-Tim*
- New fresh look
- Responsive mobile interface
- Useful admin home page
- Minimal template overriding
- Support RTL and LTR template
- Easy integration

<br />

![Django Admin Black - Template project for Django provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-admin-black/main/media/django-admin-black-intro.gif)

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

## Screenshots

![Django Admin Black - Main Django Dashboard screen.](https://raw.githubusercontent.com/app-generator/django-admin-black/main/media/django-admin-black-screen.png)

<br>

![Django Admin Black - Add user screen.](https://raw.githubusercontent.com/app-generator/django-admin-black/main/media/django-admin-black-screen-add-user.png)

<br>

![Django Admin Black - Edit user permissions.](https://raw.githubusercontent.com/app-generator/django-admin-black/main/media/django-admin-black-screen-edit-permissions.png)

<br>

---
**Django Admin Black** - Provided by **AppSeed [App Generator](https://appseed.us/)**
