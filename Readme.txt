Setup

The first thing to do is to clone the repository:

$ git clone  https://github.com/Parthasarathimca/RB_Blog.git  
$ cd Questions
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:
(env)$ python manage.py runserver
Roles
 1. User
 3. Mentor

=> create SUPER USER
=> Generate JWT Token 

http://127.0.0.1:8001/api/token/

Use that Barrer token for all end poinnts

---------------------------------------------
Custom user app created for add User

http://127.0.0.1:8001/users/ => GET and POST APIS
For add questions
---------------------------------------------
http://127.0.0.1:8001/questions/  => GET and POST APIS
For Answer questions as a mentor 
------------------------------------
http://127.0.0.1:8001/questions/  => GET and POST APIS
