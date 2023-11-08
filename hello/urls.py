from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("rahmon", views.rahmon, name="rahmon"),
    path("roheem", views.roheem, name="roheem")
]