from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from custom_users.forms import RegistrationUserForm, LoginUserForm
from main.models import PostalLetterModel


class RegisterUserView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'custom_users/registration.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': 'Регистрация'
    }

    def form_valid(self, form, backend='django.contrib.auth.backends.ModelBackend'):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(self.success_url)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'custom_users/login.html'
    extra_context = {
        'title': 'Вход'
    }


def logout_user(request):
    logout(request)
    return redirect('login')


class ProfileView(ListView):
    model = PostalLetterModel
    template_name = 'custom_users/profile.html'
    context_object_name = 'letters'
    extra_context = {
        'title': 'Профиль',
    }

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-created')


