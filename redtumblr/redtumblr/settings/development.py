from .partials import *


INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',

    'django_nose',
)


# django-extensions
# http://django-extensions.readthedocs.org

# Always use IPython for shell_plus
SHELL_PLUS = "ipython"


# django-nose
# https://django-nose.readthedocs.org

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--verbosity=2',
    '--nocapture',

    '--with-coverage',
    '--cover-package=redtumblr',
    '--cover-inclusive',
]
