import os
from .application import BASE_DIR, PROJECT_ROOT


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'dist', 'static', )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'dist', 'media', )


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', ),
    os.path.join(PROJECT_ROOT, 'dist', 'components', ),
)
