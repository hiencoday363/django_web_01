from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("scrap.urls")),
    path("login/", include("auth_acc.urls")),
    path("upload/", include("fileUpload.urls")),
    path('redis/', include("useRedis.urls")),

    path("api/", include("api_chat_video.urls")),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
