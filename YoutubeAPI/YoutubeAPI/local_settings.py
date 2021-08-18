# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!te&n&4@g5_6=2d8pio*(49f6jzeq-xbv6ys8p_h013f5h7&ux'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube',
        'USER': 'root',
        'PASSWORD': 'FocusRite!@34',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}