# Personal Boardgame Leaderboard


## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General Info 
API documentation can be found [here](https://documenter.getpostman.com/view/12316899/T1LLDnJL?version=latest).

## Technologies
The boardgame leaderboard API is built using [Django 3.0.8](https://docs.djangoproject.com/en/3.1/) and [Django Rest Framework 3.11.0](https://www.django-rest-framework.org/)


A list of all installed packages and dependencies can be found in `requirements.txt`.


## Setup
### Cloning the repository
Download or clone this repository using `git clone https://github.com/samfweb/boardgame-leaderboard.git`

### Initalising a new virtual environment
Initalise a new virtual python environment with `python3 -m venv /path/to/new/virtual/environment`
I would recommend navigating to the root directory of your project and using `python3 -m venv .`

Activate your new venv using `source <venv>/bin/activate`

### Installing packages and dependencies
After activating your virtual environment, use `pip install -r requirements.txt` to install all required dependencies.

### Setting environment variables
Some variables have been removed from `settings.py` for security reasons. 

You'll need to set them in a file named `.env` in the project's root.

An `example.venv` has been included; simply change the variables and save it as `.env` if you wish.


### Initialising the database
With your venv active and in the project's root folder, run

`./manage.py makemigrations`

`./manage.py migrate`.

This will create the SQLite database.

### Creating a superuser
Create a superuser(admin) for the leaderboard with.

`./manage.py createsuperuser`

You'll be prompted to enter details such as username and password.

## Usage

### Running the server
Spin up a local server with `./manage.py runserver`

You should see the following:
![server_success](https://i.imgur.com/nlzOfmH.png)


### Accessing the admin interface
The admin interface can be found at  

### Using the API
If debug mode is enabled, you can interact with the API using Django's browesable interface.

Full API documentation can be viewed [here](https://documenter.getpostman.com/view/12316899/T1LLDnJL?version=latest). 