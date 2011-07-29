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
* Change into the myproject directory and run ./manage deploy
* ./manage remote createsuperuser

Development
===========
* Run devutils/smtp_server.py to view outgoing emails on stdout

References
==========
* http://www.allbuttonspressed.com/projects/djangoappengine
* http://www.allbuttonspressed.com/projects/django-nonrel
