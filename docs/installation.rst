Installation
============

Prerequisites
-------------
Before you install MyParty, ensure you have the following installed:

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)

Step 1: Clone the Repository
---------------------------
$ git clone https://github.com/thabangnkhuna/myparty.git
$ cd myparty

Step 2: Set up Virtual Environment
----------------------------------
$ python -m venv venv
$ source venv/bin/activate (for Windows: venv\Scripts\activate)

Step 3: Install Dependencies
---------------------------
$ pip install -r requirements.txt

Step 4: Run Migrations
----------------------
$ python manage.py migrate

Step 5: Create Superuser (Optional)
----------------------------------
$ python manage.py createsuperuser

Step 6: Start the Development Server
-----------------------------------
$ python manage.py runserver

You're all set! Open your browser and visit http://localhost:8000 to access MyParty.
