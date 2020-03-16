# Openlab
E-Learning Website

You can view a working version of this app
[here](http://...-django.herokuapp.com) (not working yet)

# Introduction
<img src="https://github.com/A-Arari/openlab/blob/master/screenshots/screenshot-full.png">

# Installation
Assuming python 3.X istalled, follow these steps to download and run the openlab application

Install Virtualenv first

    $ pip install virtualenv
    
 Download this project, or clone it
 then navigate to this cloned directory and run:

    $ virtualenv venv
    $ "venv/scripts/activate"
    $ pip install django
    $ cd openalab
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver

* Initial data supports 3 types of users for testing purposes(change the number in email from 1-4 to use different users):
    * Students (email=student1@gmail.com, password=passmot123)
    * Professor (email=teachert1@gmail.com, password=passmot123)
    * Admin (email=admin@gmail.com, password=passmot123)
    * Visit http://127.0.0.1:8000/
