============================================
 django-nonrel and Google App Engine starter
============================================

.. contents ::

Requirements
============
* Python 2.5+
* virtualenv

Installation
=============
* virtualenv --python=python2.5 --no-site-packages .
* source bin/activate
* Include google_appengine in your PATH
* Edit line 2 in myproject/app.yaml to point to your application
* Change secret key in settings.py
* Change into the myproject directory and run python manage deploy
* Optional: python manage remote createsuperuser

Development
===========
* Run devutils/smtp_server.py to view outgoing emails on stdout

References
==========
* http://www.allbuttonspressed.com/projects/djangoappengine
* http://www.allbuttonspressed.com/projects/django-nonrel
