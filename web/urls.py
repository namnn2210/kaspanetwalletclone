from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recover", views.recover, name="recover"),
]