A collection of Django project templates
========================================

Settings configurations

* Database
* Logging
* Static files
* Registration URLs (password reset)
* Email
* Tests
* Initial user(s)
* Dev/Production status

Templates
=========

Current
-------

* Basic (one language, locale)

Planned
-------

* Django-CMS
* Multi-lingual (basic disabled i18n, l10n)
* Social

App roadmap
===========

**The actual app should be named something different than this.**

This is designed as a seed for an app that will allow you to quickly create
Django projects based on template projects, either default or user defined.

It should allow someone to:

* Create an empty one just like normal django-admin.py startproject
* Create one from a full project template (a la Pinax)
* Create one from a project template with placeholders, like regular template
  files might have

The app should use a settings file (Python, YAML, etc.) to populate certain
settings values, such as site admin name/email. It might also create a new hash
for a project secret key.

There should be a multilingual option (or a "one language" or English option).
This should include utilites for easy translation.

It should also include templates or easy configuration for app deployment
services, e.g. Gondor, ep.io, Heroku, etc.

Influences
==========

* Pinax
* Zachary Voase's Django project conventions
* Audrey Roy's django-handstand project
* Read the Docs
