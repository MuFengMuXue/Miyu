**Resources**

[[]][Home](https://www.djangoproject.com/)

[[]][Official documentation](https://docs.djangoproject.com/)

[[]][Package information](https://packages.gentoo.org/packages/dev-python/django)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Django_(web_framework) "wikipedia:Django (web framework)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/django)

[[]][GitHub](https://github.com/django/django)

**Django** is a web application framework built on [Python](https://wiki.gentoo.org/wiki/Python "Python").

See the [Django overview](https://www.djangoproject.com/start/overview/) for information on the possibilities this project offers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Apache modules]](#Apache_modules)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Starting a sample project]](#Starting_a_sample_project)
    -   [[2.2] [Production usage]](#Production_usage)

## [Installation]

### [USE flags]

### [USE flags for] [dev-python/django](https://packages.gentoo.org/packages/dev-python/django) [[]] [High-level Python web framework]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)           Add support for sqlite - embedded sql database
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 16:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-python/django`

Test if Python\'s import of django:

`user `[`$`]`python -c "import django; print(django.get_version())"`

### [Apache modules]

Apache is just one of the [setups that can be used](https://docs.djangoproject.com/en/3.2/howto/deployment/), though this is a very popular and mature web server.

When planning on using Apache for production, emerge the [WSGI](https://wsgi.readthedocs.org/en/latest/) (Web Server Gateway Interface) module:

`root `[`#`]`emerge --ask www-apache/mod_wsgi`

Enable the WSGI module in Apache\'s configuration file:

[FILE] **`/etc/conf.d/apache2`Enabling the WSGI module**

    APACHE2_OPTS="... -D WSGI"

Example to set up a given virtual host with WSGI:

[FILE] **`/etc/apache2/vhosts.d/00_myProject.conf`Specify WSGI config**

    <VirtualHost *:80>
       ...
       WSGIScriptAlias / /var/www/myProject/myProject/myProject.py
       ...
    </VirtualHost>

IMPORTANT: For some funny reason the default wsgi.py file (what you should have renamed to myProject.py, if you follow the example) created by:

`user `[`$`]`django-admin startproject myProject`

is not properly configured to work with Apache or other severs expect for Django\'s own. To fix it you must add this line in your wsgi.py file:

[FILE] **`/var/www/myProject/myProject/myProject.py`Add your project to Python\'s sys.path**

    ...
    sys.path.append('/var/www/myProject') #This is the missing line it must be before os.environ.setdefault(...)
    ...

## [Usage]

### [Starting a sample project]

As an example, and to make sure everything is working correctly, a sample project may be used. First create the project in the working directory:

`user `[`$`]`django-admin startproject myProject`

This will create a directory containing files to make up a skeleton Django project, these will be modified according to the project\'s needs. Move to the project directory:

`user `[`$`]`cd myProject`

To get a glimpse of Django in action, start the development server by running:

`user `[`$`]`python manage.py runserver`

Open a web browser and navigate to [http://127.0.0.1:8000]. This should only be accessible from the local machine, and not on any other IP addresses, but don\'t rely on this being secure. The development server will use port [8000] by default; the port can be changed by adding a chosen port number after the [runserver] command above.

** Important**\
**Do not use this development server for production!** It should **only** be used for *testing during development*.

### [Production usage]

A fully capable web server, such as [Apache](https://wiki.gentoo.org/wiki/Apache "Apache"), must be used for Django projects in production. The Django website has information on some of the [setups that can be used](https://docs.djangoproject.com/en/3.2/howto/deployment/).

See the [getting started](https://www.djangoproject.com/start/) page for links to their excellent [tutorial](https://docs.djangoproject.com/en/3.2/intro/), complete [documentation](https://docs.djangoproject.com/), and more, on the [website](https://www.djangoproject.com).