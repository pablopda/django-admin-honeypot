=====================
django-admin-honeypot
=====================

.. image:: https://travis-ci.org/dmpayton/django-admin-honeypot.svg?branch=develop
   :target: https://travis-ci.org/dmpayton/django-admin-honeypot
   :alt: Travis-CI

.. image:: https://coveralls.io/repos/dmpayton/django-admin-honeypot/badge.svg?branch=develop
   :target: https://coveralls.io/r/dmpayton/django-admin-honeypot
   :alt: Coverage

.. image:: https://codeclimate.com/github/dmpayton/django-admin-honeypot/badges/gpa.svg?branch=develop
   :target: https://codeclimate.com/github/dmpayton/django-admin-honeypot
   :alt: Code Climate

**django-admin-honeypot** is a fake Django admin login screen to log and notify
admins of attempted unauthorized access. This app was inspired by discussion
in and around Paul McMillan's security talk at DjangoCon 2011.

* **Original Author**: `Derek Payton <http://dmpayton.com/>`_
* **Current Maintainer**: `Pablo Perez De Angelis <https://github.com/pablopda>`
* **Version**: 1.2.0
* **License**: MIT

Features
========

* Captures unauthorized login attempts
* Notifies admins of unauthorized access attempts
* Compatible with Django 3.0, 3.1, 3.2, and 4.0
* Supports Python 3.6, 3.7, 3.8, and 3.9

Documentation
=============

http://django-admin-honeypot.readthedocs.io

Quick Start
===========

1. Install django-admin-honeypot from PyPI:

   .. code-block:: bash

       pip install django-admin-honeypot

2. Add ``admin_honeypot`` to your ``INSTALLED_APPS`` in settings.py:

   .. code-block:: python

       INSTALLED_APPS = [
           ...
           'admin_honeypot',
           ...
       ]

3. Update your urls.py:

   .. code-block:: python

       from django.contrib import admin
       from django.urls import path, include

       urlpatterns = [
           ...
           path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
           path('secret/', admin.site.urls),
       ]

   NOTE: Replace ``secret`` in the url above with your own secret url prefix

4. Run migrations:

   .. code-block:: bash

       python manage.py migrate

Configuration
=============

By default, django-admin-honeypot will send an email to all staff users when an unauthorized access attempt is made. You can customize this behavior by adding the following settings to your project's settings.py:

.. code-block:: python

    # Disable email notifications
    ADMIN_HONEYPOT_EMAIL_ADMINS = False

    # Custom email subject
    ADMIN_HONEYPOT_EMAIL_SUBJECT = 'Custom Admin Honeypot Subject'

Contributing
============

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository and clone it locally
2. Create a new branch for your feature or bug fix
3. Write tests for your changes
4. Run the tests with `tox`
5. If the tests pass, submit a Pull Request

License
=======

django-admin-honeypot is released under the MIT License. See the bundled `LICENSE` file for details.