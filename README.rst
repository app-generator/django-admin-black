=====
Django Admin Black
=====

**Modern template for Django admin interface**

Why Django Admin Black?
===============

* UI Kit: **[Black Dashboard](https://www.creative-tim.com/product/black-dashboard?AFFILIATE=128200)** (Free version) provided by **Creative-Tim**
* New fresh look
* Responsive mobile interface
* Useful admin home page
* Minimal template overriding
* Support RTL and LTR template
* Easy integration

Screenshots
===========

.. image:: https://creativetimblog.com/blog/wp-content/uploads/2019/08/Django-Template%E2%80%93-Black-Dashboard-730x410.png
    :alt: Screenshot #1
    :align: center
    :target: https://creativetimblog.com/blog/wp-content/uploads/2019/08/Django-Template%E2%80%93-Black-Dashboard-730x410.png

Installation
============

* Download and install latest version of Django Admin Black:

.. code:: python

    pip install git+https://github.com/app-generator/django-admin-black.git
    # or
    easy_install git+https://github.com/app-generator/django-admin-black.git

* Add 'admin_black' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

.. code:: python

    INSTALLED_APPS = (
        ...
        'admin_black.apps.AdminBlackConfig',
        'django.contrib.admin',
    )

..

 All programs you add in INSTALLED_APPS should look like this: "APP_NAME.apps.APP_NAMEConfig".

 In this feature, we considered that each App can have its own icon, so we ask users to use this feature according to the method. Also in apps.py of each program according to the example add the icon field in the corresponding class.

 You can go <https://django-dashboard-black.appseed.us/ui-icons.html> to use more icons

.. code:: python

    from django.apps import AppConfig

    class APP_NAMEConfig(AppConfig):
        name = 'APP_NAME'
        icon = 'ICON_CLASS'  # for example: icon = 'tim-icons icon-atom'

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+ way):

.. code:: python

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

.. warning::
    Before Django 1.8 you should specify context processors different way. Also use ``django.core.context_processors.request`` instead of ``django.template.context_processors.request``.

    .. code:: python

        from django.conf import global_settings

        TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
            'django.core.context_processors.request',
        )

* Create database tables:

.. code:: python

    python manage.py migrate admin_black
    # or 
    python manage.py syncdb
        
* Collect static if you are in production environment:

.. code:: python

        python manage.py collectstatic
        
* Clear your browser cache
