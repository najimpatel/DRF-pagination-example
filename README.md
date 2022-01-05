# DRF-pagination
DRF pagination using pageNumberPagination

This is a simple API for:

Running Locally
Must have Python 3 & django djangorestframework installed and running
Clone the repo and cd into repo

Create a virtual environment: python -m venv page

Go into your virtual environment: page\scripts\activate

Install dependencies: pip install -r requirements.txt

creating student model in models.py file 

Run makemigrations: python manage.py makemigrations
Run migrations: python manage.py migrate
Create an admin user for logging into the Django admin interface: python manage.py createsuperuser
Setup Database

Run the app: python manage.py runserver
View the API at localhost:8000 and the admin interface at localhost:8000/api/


check student list:

http://127.0.0.1:8000/api/

http://127.0.0.1:8000/api/?pageNum=2&rows=3 and so on...
