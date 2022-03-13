from django.urls import path

from . import views

urlpatterns = [
    path("add/<int:id>/<int:usere>/",views.like_add, name="like")
]