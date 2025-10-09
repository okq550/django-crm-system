The "externally-managed-environment" error means your system Python is protected from direct package installations (common on macOS/Linux to prevent conflicts with system packages). Solution: Use a virtual environment
Create a virtual environment (in your project directory):
cd /Users/sam/code/src/github.com/okq550/PROJECTS/Salat
python3.13 -m venv venv
Activate it:

source venv/bin/activate
Install Django:
pip install Django
Deactivate when done:
deactivate

# Install postgresDriver
pip install "psycopg[binary]"

git init
git add .
git commit -m "first commit"
git remote add origin git@okq550-github:okq550/django-crm-system.git
git push -u origin main

# Running the App
source venv/bin/activate
python manage.py runserver

# Creating Apps
$ python manage.py startapp polls


# Structure of the Framework
Project (mysite)

mysite is your Django project's root configuration directory
It contains core settings and routing for your entire web application
Key files:
settings.py: Global configuration (database, installed apps, middleware, etc.)
urls.py: Main URL routing configuration
wsgi.py/asgi.py: Web server entry points
App (polls)

polls is a Django application - a self-contained module for specific functionality
Apps are reusable components that serve a single purpose
Key files:
models.py: Database models/tables
views.py: Request handlers/controllers
urls.py: URL routing specific to this app
admin.py: Admin interface configuration

# Install libraries
srouce venv/bin/activate
pip install "psycopg[binary]"

# Create App
python manage.py startapp polls

# Make Migrations
Add the polls app in INSTALLED_APPS in settings.py
python manage.py makemigrations polls

# See Migration SQL statements
python manage.py sqlmigrate polls 0001

# Migrate 
python manage.py migrate

# Run the shell
python manage.py shell

# Create the admin user
python manage.py createsuperuser

# Install Django Debug Toolbar
python -m pip install django-debug-toolbar