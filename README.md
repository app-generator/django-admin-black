# [Django Admin Black](https://appseed.us/product/black-dashboard/django/)

Modern template for **Django** that covers `Admin Section`, all authentication pages (registration included) crafted on top of **[Black Dashboard](https://appseed.us/product/black-dashboard/django/)**, an open-source `Bootstrap 5` design from [Creative-Tim](https://www.creative-tim.com/?AFFILIATE=128200).

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- [Django Black Dashboard](https://appseed.us/product/black-dashboard/django/) - `Product` that uses the library
  - `Features`: Fully-configured, `CI/CD` via Render
- UI Kit: [Black Dashboard](https://www.creative-tim.com/product/black-dashboard?AFFILIATE=128200) `free version` by Creative-Tim
- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Registration` page
  - `Misc pages`: colors, icons, typography, blank-page 
  
<br />

![Django Admin Black - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/196730732-dda1794b-93ce-48cb-bc5c-182411495512.png)

<br />

## Why `Django Black Design`

- Modern [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

<br />

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-black
// OR
$ pip install git+https://github.com/app-generator/django-admin-black.git
```

<br />

> Add `admin_black` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_black.apps.AdminBlackConfig',
        'django.contrib.admin',
    )
```

<br />

> Add `admin_black` urls in your Django Project `urls.py` file.

```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_black.urls')),
    ]
```

<br />

> **Collect static** if you are in `production environment`:

```bash
$ python manage.py collectstatic
```

<br />

> **Start the app**

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## How to Customize 

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The  theme used to style this starter provides the following files: 

```bash
# This exists in ENV: LIB/admin_black
< UI_LIBRARY_ROOT >                      
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- auth-signin.html     # Sign IN Page
   |    |    |-- auth-signup.html     # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |
   |    |-- pages/       
   |         |-- dashboard.html       # Dashboard page
   |         |-- user.html            # Settings  Page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

For instance, if we want to customize the `dashboard.html` these are the steps:

- `Step 1`: create the `templates` DIRECTORY inside your app 
- `Step 2`: configure the project to use this new template directory
  - Edit `settings.py` TEMPLATES section 
- `Step 3`: copy the `dashboard.html` from the original location (inside your ENV) and save it to the `YOUR_APP/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_black/pages/dashboard.html`
  - Destination PATH: `YOUR_APP/templates/pages/dashboard.html`
- Edit the footer (Destination PATH)    

At this point, the default version of the `dashboard.html` shipped in the library is ignored by Django.

In a similar way, all other files and components can be customized easily.

<br />

## Recompile SCSS  

The SCSS/CSS files used to style the Ui are saved in the `admin_black/static/assets` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn # install modules
$ # # edit variables 
$ vi static/assets/scss/black-dashboard/custom/_variables.scss 
$ gulp # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$default:       #344675 !default; // EDIT for customization
$primary:       #e14eca !default; // EDIT for customization
$secondary:     #f4f5f7 !default; // EDIT for customization
$success:       #00f2c3 !default; // EDIT for customization
$info:          #1d8cf8 !default; // EDIT for customization
$warning:       #ff8d72 !default; // EDIT for customization
$danger:        #fd5d93 !default; // EDIT for customization
$black:         #222a42 !default; // EDIT for customization
```

<br />

## [PRO Version](https://appseed.us/product/black-dashboard-pro/django/)   

This design is a pixel-perfect [Bootstrap](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design. 
Black is a completly new product built on our newest re-built from scratch framework structure that is meant to make our products more intuitive, more adaptive and, needless to say, so much easier to customize. 

> Features: 

- `Up-to-date Dependencies`
- `Design`: Django Theme Black - `PRO Version`
- `Sections` covered by the design:
  - **Admin section** (reserved for superusers)
  - **Authentication**: `Django.contrib.AUTH`, Registration
  - **All Pages** available in for ordinary users 
- `Docker`, `Deployment`:
  - `CI/CD` flow via `Render`

<br />

![Django Black PRO - Premium Seed project powered by Flask.](https://user-images.githubusercontent.com/51070104/187623954-c4ade6a0-8cb2-4d2e-8698-e962621a613c.png)

<br />

---
**[Django Admin Black](https://appseed.us/product/black-dashboard/django/)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
