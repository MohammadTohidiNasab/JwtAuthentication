from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    first_name = models.models.CharField(max_length=255)
    last_name = models.models.CharField(max_length=255)
    email = models.models.CharField(max_length=255,unique=True)
    password = models.models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()