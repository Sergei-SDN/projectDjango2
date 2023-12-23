from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import CustomUser


# Create your views here.


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    if form_class.is_valid():
        form_class.save()
        verify_email()
        return redirect ('confirm_email')




class ProfileView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'users/users_form.html'

    def get_object(self, queryset=None):
        return self.request.user
