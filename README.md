# Openlab
E-Learning Website

There is no live version, yet. To run the project, follow the instructions bellow.

# Screenshot
<img src="https://github.com/A-Arari/openlab/blob/master/screenshots/screenshot-full.png">

# Installation
#### Assuming python 3.X istalled :

Install Virtualenv first by

    $ pip install virtualenv
    
Clone the porject using git (install git if you didn't)

    $ git clone https://github.com/A-Arari/openlab.git

Navigate to this cloned directory and run:

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
    
# WYSIWYG editor used:
   CKEditor see [ckeditor.com](https://ckeditor.com/docs/ckeditor5/latest/index.html)
