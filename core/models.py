from django.db import models


class AppSetting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
