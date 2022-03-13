from .models import Post
from django.forms import ModelForm


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','img')