from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import UserProfile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    def get(self, request):
        # Отримання профілю поточного користувача
        user = get_object_or_404(UserProfile, id=request.user.id)
        return render(request, 'user_profiles/profile.html', {'user': user})


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['username', 'email', 'bio', 'avatar']
    template_name = 'user_profiles/update_profile.html'
    success_url = reverse_lazy('user_profiles:profile')

    def get_object(self):
        return self.request.user
