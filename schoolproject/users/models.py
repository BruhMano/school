from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    image = models.ImageField(upload_to="media", blank = False, null = False)
    desc = models.TextField(default="Hello. Nice to meet u!", max_length=30)
    
