from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='upload'),
    # path('download/', views.show_down, name='download'),
    path('list', views.ListModelView.as_view(), name='list_model'),
    path('list/<int:pk>', views.DetailModelView.as_view(), name='detail_model'),
    path('active', views.GetIdFileAPIView.as_view(), name='get_acive_model'),
]