from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ("id","title", "pub_date", "author","img") 
    search_fields = ("title",) 
    list_filter = ("pub_date",) 

admin.site.register(Post, PostAdmin)
