from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nancai_teacher',
        'USER': 'root',
        'PASSWORD': 'zxk123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}