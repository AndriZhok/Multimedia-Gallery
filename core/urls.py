from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppSettingViewSet

router = DefaultRouter()
router.register(r'', AppSettingViewSet, basename='appsetting')

urlpatterns = [
    path('', include(router.urls)),
]