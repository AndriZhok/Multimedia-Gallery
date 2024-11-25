from django.urls import path
from .views import UserProfileView, UserProfileUpdateView

app_name = 'user_profiles'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='update'),
]
