from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import AppSetting
from .serializers import AppSettingSerializer


class AppSettingViewSet(viewsets.ModelViewSet):
    queryset = AppSetting.objects.all()
    serializer_class = AppSettingSerializer

    def perform_update(self, serializer):
        serializer.save()

    def get(self, request):
        settings = AppSetting.objects.all()
        return render(request, 'core/settings.html', {'settings': settings})
