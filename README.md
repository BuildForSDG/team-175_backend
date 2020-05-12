# backend_sdg
backend SGG

This API will work efficiently under python 3.6.0.
Ensure you have installed all the requirements in the requirements.txt file as well.

# Django 1.11 project template

This is a simple Django 1.110+ project template with my preferred setup. Most Django project templates make way too many assumptions or are just way too complicated. I try to make the least amount of assumptions possible while still trying provide a useful setup. Most of my projects are deployed to Heroku, so this is optimized for that but is not necessary.


## How to install

1. create a folder on your desktop
2. open git bash and navigate to the created folder 
3. clone the project
4. create another folder outside the clone project and name it 'backend'
5. move your cloned project project to the 'backend' folder
6. open a terminal and navigate to the backend folder
7. create a virtual environment and activate it:<br>
  (for window users)<br>
  i) creating vitual environment<br>
    -> python -m venv sdgVenv
  ii) activating virtual environment
    -> sdgVenv\Scripts\activate.bat
8. run the following commands to install the required packages on your terminal:
  -> pip install django==1.11
  -> pip install djangorestframework==3.8.2
  -> pip install django-rest-auth
  -> pip install djangorestframework-jwt
9. cd in to 'team_175_backend' on your terminal
9. run makemigrations command -> python manage.py makemigrations
10. run migrate command -> python manage.py migrate
11. start the server -> python manage.py runserver
13. navigate to different urls on the api:
  i) to see all application users and possible CRUD functionalities 
    ->localhost:8000/api/users/
  ii) to see the login option
    ->localhost:8000/api/auth/login
  iii)to see other auth options
    ->localhost:8000/api/auth
    -> 
14. To log in to admin account, create superuser.
    Go back to terminal and stop the server
15. Create superuser
    -> python manage.py createsuperuser
16. Start the server again and go to this url on the browser
  -> localhost:8000/admin
 17. Login with the user username and password you used in the creation of the super user.
