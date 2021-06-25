import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }

pytest_plugins = (
    'api.tests.fixtures',
  )
