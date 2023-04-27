import os

from django.db import IntegrityError
from django.contrib.auth.models import User

env = os.environ

try:
    superuser = User.objects.create_superuser(
        username=env["ADMIN_USERNAME"],
        email=env["ADMIN_EMAIL"],
        password=env["ADMIN_PASSWORD"])
except IntegrityError:
    print(f"Super User with username {env('SUPER_USER_NAME')} is already exit!")
except Exception as e:
    print(e)
