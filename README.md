# Django Admin Black

Modern template for **Django admin interface** coded in **Django Framework**

> Originally coded by [Iman Karimi](https://github.com/imankarimi), actively versioned and supported by [AppSeed](https://appseed.us/). 
For support please use Github (issues tracker) or chat with AppSeed support team on [Discord](https://discord.gg/fZC6hup) - 24/7 LIVE Service.

<br>

**Links & Resources**

- [Django Black Dashboard](https://appseed.us/admin-dashboards/django-dashboard-black) - Open-source starter that uses the same UI Kit
- [Django Black Dashboard - DEMO](https://django-dashboard-black.appseed.us/login/) - LIVE Deployment

<br />

## Why Django Admin Black?

- UI Kit: **Black Dashboard** (Free version) provided by **Creative-Tim**
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

---
**Django Admin Black** - Provided by **[AppSeed](https://appseed.us/)**
