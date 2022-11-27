from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.scrap.urls")),
    path("login/", include("apps.auth_acc.urls")),
    # path("upload/", include("apps.fileUpload.urls")),
    path('redis/', include("apps.useRedis.urls")),
    
    path('model3d/', include("apps.fileUpload.urls")),

    path("api/", include("apps.api_chat_video.urls")),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
