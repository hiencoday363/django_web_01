from django.urls import path

from apps.auth_acc import views

urlpatterns = [
  path('', views.SiteLogin.as_view(), name='login'),
  # path('', views.CustomLogin, name='login'),
  path('register', views.SiteRegister , name='register'),
  path('logout/', views.SiteLogout , name='logout'),
  path('profile/', views.SiteProfile.as_view(), name='profile'),
  path('profile/get/', views.chatbot_res),

]