from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    author = models.ForeignKey(user, on_delete = models.CASCADE)
    img = models.ImageField()
    pub_date = models.DateField(auto_now=True)



