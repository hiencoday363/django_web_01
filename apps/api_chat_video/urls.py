from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import checkLogin, GetImageAPIView, UploadImageApiView, UploadImageDetail, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
    # path('', checkLogin, name='api'),

    path('upload/auth/', obtain_auth_token),

    path('upload/create/', include(router.urls)),

    path('upload/image/', GetImageAPIView.as_view()),
    path('create/image/', UploadImageApiView.as_view()),
    path('upload/image/<int:id>/', UploadImageDetail.as_view()),

    # path('upload/', UploadViewSet.as_view({'post': 'create'}), name='create'),
    # path('get/upload/', UploadViewSet.as_view({'get': 'list'}), name='upload'),
    # path('upload/', upload_serializer, name='upload'),
]
