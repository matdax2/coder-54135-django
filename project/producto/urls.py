from django.urls import path

app_name = "producto"

from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
