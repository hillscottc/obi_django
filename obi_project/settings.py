"""
Django settings for obi_project project.
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4*@q9i)w)q+t775qf&=^jp_lj%*y_6+_g#^t502$3@e=g5$-0u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'obi_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'obi_project.urls'
WSGI_APPLICATION = 'obi_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'obi_app', 'templates'),
]

SITE_NAME = "Obi Site"

PROJECT_APPS = ('obi_app', )

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    # 'django_jenkins.tasks.django_tests',   # select one django or
    # #'django_jenkins.tasks.dir_tests'      # directory tests discovery
    'django_jenkins.tasks.run_pep8',
    # 'django_jenkins.tasks.run_pyflakes',
    # 'django_jenkins.tasks.run_jslint',
    # 'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount',
    'django_jenkins.tasks.run_graphmodels',
)


# ## In the heroku environ this will be set
# if 'DATABASE_URL' in os.environ:
#     import dj_database_url
#     DATABASES['default'] = dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')