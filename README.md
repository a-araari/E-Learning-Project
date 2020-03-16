# Openlab
E-Learning Website

There is no live version, yet. To run the project, follow the instructions bellow.

# Screenshot
<img src="https://github.com/A-Arari/openlab/blob/master/screenshots/screenshot-full.png">

# Installation
#### Assuming python 3.X installed :

Open your command line and install Virtualenv by typing

    $ pip install virtualenv
    
Clone the porject using git (install [git](https://github.com/git-for-windows/git/releases/download/v2.25.1.windows.1/Git-2.25.1-64-bit.exe) if you didn't, or simply download is and extract it)

    $ git clone https://github.com/A-Arari/openlab.git

Navigate to the parent directory(openlab) and run:

    $ virtualenv venv
    $ "venv/scripts/activate"
    $ cd openlab
    $ pip install -r requirements.txt
    $ py manage.py runserver
    
Now Visit http://127.0.0.1:8000/

* Initial data supports 3 types of users for testing purposes(change the number in email from 1-4 to use different users):
    * Students (email=student1@gmail.com, password=passmot123)
    * Professor (email=teachert1@gmail.com, password=passmot123)
    * Admin (email=admin@gmail.com, password=passmot123)
    
## WYSIWYG editor used:
   CKEditor see [ckeditor.com](https://ckeditor.com/docs/ckeditor5/latest/index.html)
