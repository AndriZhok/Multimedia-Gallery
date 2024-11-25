from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import MediaFile
from media_files.serializers import MediaFileSerializer


class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

    def get(self, request):
        media_files = MediaFile.objects.all()
        return render(request, 'media_files/list.html', {'media_files': media_files})
