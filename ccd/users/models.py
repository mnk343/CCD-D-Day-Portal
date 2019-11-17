from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length = 200 , blank = False)
