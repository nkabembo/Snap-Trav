from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    #Other user fields username, email and password will come from AbstractUser since they are built-in
    preferences = models.JSONField(blank=True,null=True)

    def __str__(self):
        return self.username


