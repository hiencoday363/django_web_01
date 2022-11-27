from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='postcar'),
    path('<int:id>/', detaiCar, name='detailcar'),
]