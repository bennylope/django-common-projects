====================
Basic Django project
====================

**NOTE**: the settings file has been turned into a module, which makes
management of different settings files easier across multiple environments. It
means, however, that the chosen module must explicitly be called when using
Django managmeent commands. E.g.

::

    ./manage.py syncdb --settings=settings.dev
    ./manage.py migrate --settings=settings.dev
    ./manage.py runserver --settings=settings.dev


Installation
============

1. Ensure you have activate a virtualenvironment with the `--no-site-packages`
   flag.

2. Install the requirements.

   ::

        pip install --requirement requirements/project.txt

3. Sync the database

   ::

        ./manage.py syncdb --settings=settings.dev

4. Migrate South's schema changes

   ::

        ./manage.py migrate --settings=settings.dev

5. Run the dev server

   ::

        ./manage.py runserver --settings=settings.dev

Adding additional apps
======================

