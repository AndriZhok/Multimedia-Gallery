from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_profile_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_profile_permissions",
        blank=True,
    )
