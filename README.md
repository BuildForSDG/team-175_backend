# backend_sdg
backend SGG

This API will work efficiently under python 3.6.0.
Ensure you have installed all the requirements in the requirements.txt file as well.

# Django 1.11 project template

This is a simple Django 1.110+ project template with my preferred setup. Most Django project templates make way too many assumptions or are just way too complicated. I try to make the least amount of assumptions possible while still trying provide a useful setup. Most of my projects are deployed to Heroku, so this is optimized for that but is not necessary.


## How to install

1. create a folder on your desktop <br>
2. open git bash and navigate to the created folder <br>
3. clone the project <br>
4. create another folder outside the clone project and name it 'backend' <br>
5. move your cloned project project to the 'backend' folder<br>
6. open a terminal and navigate to the backend folder<br>
7. create a virtual environment and activate it:<br>
  (for window users)<br>
  i) creating vitual environment<br>
    -> python -m venv sdgVenv<br>
  ii) activating virtual environment<br>
    -> sdgVenv\Scripts\activate.bat<br>
8. run the following commands to install the required packages on your terminal:<br>
  -> pip install django==1.11<br>
  -> pip install djangorestframework==3.8.2<br>
  -> pip install django-rest-auth<br>
  -> pip install djangorestframework-jwt<br>
9. cd in to 'team_175_backend' on your terminal<br>
9. run makemigrations command<br>
  -> python manage.py makemigrations <br>
10. run migrate command<br> 
  -> python manage.py migrate<br>
11. start the server -> python manage.py runserver<br>
13. navigate to different urls on the api:<br>
  i) to see all application users and possible CRUD functionalities<br> 
    ->localhost:8000/api/users/<br>
  ii) to see the login option<br>
    ->localhost:8000/api/auth/login<br>
  iii)to see other auth options<br>
    ->localhost:8000/api/auth<br>
14. To log in to admin account, create superuser.
    Go back to terminal and stop the server<br>
15. Create superuser<br>
    -> python manage.py createsuperuser<br>
16. Start the server again and go to this url on the browser<br>
  -> localhost:8000/admin<br>
 17. Login with the user username and password you used in the creation of the super user.
