"""
WSGI config for quiz_gen_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

import subprocess
result = subprocess.run(["pip", "list"], capture_output=True, text=True)
installed_packages = result.stdout
print(installed_packages)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_gen_django.settings")

application = get_wsgi_application()

app = application