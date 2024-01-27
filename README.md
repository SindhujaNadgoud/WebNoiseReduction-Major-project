# User Login and Register system implementation in django 

## Virtualenv & Dependencies

Create  a virtualenv and run requirements.txt<br/>
<b>virtualenv</b>

<pre>pip install virtualenv</pre>

<b> what is virtual environment ? </b><br/>
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.
<br/>
<a href="https://www.geeksforgeeks.org/python-virtual-environment/" >read more... </a>

to run requirements.txt

<pre>$ pip install -r requirements.txt</pre>

here <b>env/</b> folder contains all dependencies

## Running locally of the project 

<ol>
  <li>
      clone repository 
      <pre>$ git clone https://github.com/NoiseDetection/user_login_and_register.git</pre>
  </li>
  <li>
     make database settings and connect it to your local database 
    <pre>$ cd ./src/iert </pre>
    open <b>settings.py</b> file
    <pre>
                DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "iert",
                "USER": "root",
                "HOST": "localhost",
                "PASSWORD": "NoiseDetection",
                "PORT": "3306",
                "OPTIONS": {"sql_mode": "traditional"},
            }
        }
   </pre>
   set this part according to needs.
  </li>
  <li>
    run migrations 
    <pre>$ python manage.py migrate</pre>
  </li>
  <li>
    now, runserver 
    <pre>$ python manage.py runserver</pre>
  </li>
 </ol>


### Implement Token Authentication using Django REST Framework

Token authentication refers to exchanging username and password for a token that will be used in all subsequent requests so to identify the user on the server side.This article revolves about implementing token authentication using Django REST Framework to make an API. The token authentication works by providing token in exchange for exchanging usernames and passwords.

---
<b>install django rest_framework</b>
<pre>$ pip install djangorestframework</pre>

read more at <a href="https://www.geeksforgeeks.org/implement-token-authentication-using-django-rest-framework/">geeksforgeeks</a>

---
### To run the StandAlone Application

StandAlone Application runs the Tkinter application which is under Stand_Alone Folder
---
<b>python RWDN.py</b>
---
