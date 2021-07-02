from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from scrap import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('scrap.urls')),

    path('login/', include('auth_acc.urls')),

    path('api/', include('api_chat_video.urls'))
]
