from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.cache import cache

from .models import *


# Create your views here.

def home(request):
    carDetails = CarDetail.objects.all()

    context = {
        "carDetails": carDetails
    }

    return render(request, template_name="postCar/listPost.html", context=context)

def detaiCar(request, id):
    # { % csrf_token %}
    #  cache.set("foo", "bar", timeout=22)
    return HttpResponse('You have to install redis first, if installed please fix this in views/useredis/this project')
    '''
    if cache.get(id):
        car = cache.get(id)
        print("from redis")
    else:
        try:
            car = CarDetail.objects.get(id=id)
            print('from local db')
            cache.set(id, car, timeout=120)
        except CarDetail.DoesNotExist:
            return redirect('postcar')

    context = {
        'car': car
    }
    return render(request, template_name="postCar/detail.html", context=context)
    '''