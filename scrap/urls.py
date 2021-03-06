from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('technology/', views.tech, name='technology'),
    path('business/', views.business, name='business'),
]