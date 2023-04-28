import os

from django.contrib.auth.models import User

env = os.environ

try:
    superuser = User.objects.create_superuser(
        username=env["ADMIN_USERNAME"],
        email=env["ADMIN_EMAIL"],
        password=env["ADMIN_PASSWORD"])
except Exception as e:
    print("Superuser already exists...")
