from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class ExtendedUser(AbstractUser):
    image = models.ImageField(upload_to="media", blank = False, null = False)
    desc = models.TextField(default="Hello. Nice to meet u!", max_length=30)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        img = img.resize((300,300))
        img.save(self.image.path)
    
