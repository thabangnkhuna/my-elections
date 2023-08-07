Configuration
=============

MyParty is built using Django, and the application can be configured through various settings and environment variables.

Database Configuration
----------------------
By default, MyParty uses the SQLite database. You can change the database settings in the `settings.py` file.

Example settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mypartydb',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Email Configuration
-------------------
To configure email settings, update the `settings.py` file with your SMTP server details.

Example settings:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

For more configuration options, refer to the Django documentation.

Custom Settings
---------------
If you need to add custom settings for your application, create a `settings.py` file in the project's root directory and import it in the main `settings.py`.

Example custom settings:

# settings.py
ENABLE_FEATURE_X = True
MAX_PARTY_GUESTS = 50

# main settings.py
from myparty.settings import ENABLE_FEATURE_X, MAX_PARTY_GUESTS

Be sure to handle sensitive information securely and avoid hardcoding sensitive data in configuration files.
