from rest_framework import serializers, viewsets
from .models import AppSetting


class AppSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSetting
        fields = '__all__'


class AppSettingViewSet(viewsets.ModelViewSet):
    queryset = AppSetting.objects.all()
    serializer_class = AppSettingSerializer
