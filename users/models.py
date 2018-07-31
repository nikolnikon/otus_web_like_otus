from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about = models.TextField(null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
