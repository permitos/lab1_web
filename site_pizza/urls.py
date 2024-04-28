from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("foodobjects", views.get_foodobject, name="foodobjects"),
]