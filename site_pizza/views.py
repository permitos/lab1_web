from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Food, BlogPost
from django.views.decorators.cache import cache_page
from asgiref.sync import sync_to_async

@cache_page(60 * 15)
def index(request):
    return render(request, "site_pizza/index.html")

@cache_page(60 * 15)
def menu(request):
    food_list = Food.objects.order_by()
    context = {"food_list": food_list}
    return render(request, "site_pizza/menu.html", context)

@cache_page(60 * 15)
def blog(request):
    blogpost_list = BlogPost.objects.order_by("-public_date").filter(actual_status=True)
    context = {"blogpost_list": blogpost_list}
    return render(request, "site_pizza/blog.html", context)

@cache_page(60 * 15)
def about(request):
    return render(request, "site_pizza/about.html")

@sync_to_async
def get_food_objects():
    return list(Food.objects.all())

async def get_foodobject(request):
    food_objects = await get_food_objects()
    data = [{'name': food.name, 'description': food.description, 'price': food.price} for food in food_objects]
    return JsonResponse({'food_data': data})
