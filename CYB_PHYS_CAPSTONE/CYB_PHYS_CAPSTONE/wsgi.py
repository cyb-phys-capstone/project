"""
WSGI config for CYB_PHYS_CAPSTONE project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CYB_PHYS_CAPSTONE.settings")

application = get_wsgi_application()
