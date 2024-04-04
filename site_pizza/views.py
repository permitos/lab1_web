from django.shortcuts import render
from django.http import HttpResponse
from .models import Food, BlogPost

def index(request):
    return render(request, "site_pizza/index.html")

def menu(request):
    food_list = Food.objects.order_by()
    context = {"food_list": food_list}
    return render(request, "site_pizza/menu.html", context)

def blog(request):
    blogpost_list = BlogPost.objects.order_by()
    context = {"blogpost_list": blogpost_list}
    return render(request, "site_pizza/blog.html", context)

def about(request):
    return render(request, "site_pizza/about.html")
