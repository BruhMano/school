from django.contrib import admin
from .models import ExtendedUser
from django.contrib.auth.admin import UserAdmin

class ExtendedUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "image","email") 
    search_fields = ("username",)  
    empty_value_display = "-пусто-"
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('image','desc')}),
    )


admin.site.register(ExtendedUser, ExtendedUserAdmin)