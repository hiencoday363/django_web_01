from django.urls import path, include

from .views import checkLogin, getFullAcc

urlpatterns = [
    path('', checkLogin, name='login'),
    path('getFullAcc/', getFullAcc, name='getFullAcc'),
]
