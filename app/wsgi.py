import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from . import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
