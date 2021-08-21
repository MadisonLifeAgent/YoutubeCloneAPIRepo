# Extension of settings.py that will be gitignored
# Recloned projects will not include this file!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4htsmahjlp$&p8ty_49wok+q)wz6fq(v@@1^%g=o1=b%(p-5he'

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
