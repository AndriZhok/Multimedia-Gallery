from django.db import models
from django.contrib.auth.models import User


class MediaFile(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='media_files')
    file = models.FileField(upload_to='uploads/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
