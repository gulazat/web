from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.FileField(upload_to='avatar/')
    mobile = models.CharField(blank=True, null=True, max_length=13)
    subscribe = models.BooleanField(default=False)

    class Meta:
        db_table = "d_user"
