# YoutubeCloneAPIRepo
Youtube Clone API Repo

## Description
An API built for storing comments and replies on YouTube videos. Built in Python using Django.

## Installation and Setup Instructions

#### Requirements
Python 3.9
Pipenv 2021.5.29
MySQL
Working internet connection

1. Installation
Download the repository and unzip the file into the directory you want the application to run from.

2. Prerequisite setup
Create a MySQL database. The default for this project is called youtube, with a host of 127.0.0.1 and port of 3306. Note the password used to create the database, as this will be necessary for creating the local settings.
These values can be changed as long as the local_settings.py file you create (details below) reflect the changes.
No additional steps are needed for the database, the application will complete the remainder of the setup.

Create a file in the inner youtube directory called "local_settings.py".
The structure of this file should be similar to the details provided below in order to run the application properly.

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = <A SECRET KEY CREATED SPECIFICALLY FOR YOUR APPLICATION>

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django', # default
        'NAME': 'youtube', # default
        'USER': <YOUR MYSQL USERNAME>,
        'PASSWORD': <YOUR MYSQL PASSWORD>,
        'HOST': '127.0.0.1', # default value
        'PORT': '3306', # default value
        'OPTIONS': {
            'autocommit': True
        }
    }
}
```
To create a secret key, run these commands in a terminal:
```
pip install django
python3
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key)
```
Copy the created secret key and paste it into the local_settings.py file.


3. Command line setup
Navigate to the repository in a terminal, and run the following commands:

```
pipenv install
pipenv shell
cd YouTubeAPI
python manage.py migrate
python manage.py runserver
```
everal of these commands will take some time to fully execute. This is normal, the project is being installed and set up.

Pipenv install and shell will download any required packages to the file directory, and prepare the terminal to run the following commands.
cd YouTubeAPI will navigate to the appropriate directory within the project.
Migrate will configure the database.
Lastly, runserver will set up the server to run locally, and can be accessed at the location provided in localsettings.py.

## Application Usage
Any time a new terminal is started to run the application, the command ```pipenv shell``` must be run. 
To start the application, run the command ```python manage.py runserver``` from within the outer "trash_collector" folder. This will not open a browser- it only starts the server the application runs from.
To close the application, hold CTRL and press C. This will force the server to stop, but the page will still be displayed in your browser.

Once the application is running, it is ready to receive requests!