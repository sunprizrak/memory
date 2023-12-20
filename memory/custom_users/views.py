from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, ListView
from custom_users.forms import RegistrationUserForm, LoginUserForm, PasswordEditForm
from custom_users.tokens import account_activation_token
from main.models import PostalLetterModel
from .mixins import UnauthorizedRequiredMixin


def activate_email(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('custom_users/template_activate_account.html', {
        'user': user.email,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })

    email = EmailMessage(mail_subject, message, to=[to_email])

    if email.send():
        messages.success(request, f'Что бы завершить регистрацию,\n перейдите на свой адрес электронной почты {to_email} \n \
            и перейдите по ссылке завершения регистрации.')
    else:
        messages.error(request, f'Проблема с отправкой письма с подтверждением на адрес {to_email}. Проверьте, правильно ли вы его ввели.')


def activate(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Благодарим вас за подтверждение по электронной почте. Теперь вы можете войти в свою учетную запись.')
        return redirect('login')
    else:
        messages.error(request, 'Ссылка активации недействительна!')

    return redirect('home')


class RegisterUserView(UnauthorizedRequiredMixin, CreateView):
    form_class = RegistrationUserForm
    template_name = 'custom_users/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация'
    }

    def form_valid(self, form, backend='django.contrib.auth.backends.ModelBackend'):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        activate_email(self.request, user, form.cleaned_data.get('email'))
        return HttpResponseRedirect(self.success_url)


class LoginUserView(UnauthorizedRequiredMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'custom_users/login.html'
    extra_context = {
        'title': 'Вход'
    }


def logout_user(request):
    logout(request)
    return redirect('login')


class PasswordEditView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordEditForm
    login_url = 'login'
    template_name = 'custom_users/password_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Пароль обновлён успешно!')
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = PostalLetterModel
    login_url = 'login'
    template_name = 'custom_users/profile.html'
    context_object_name = 'letters'
    extra_context = {
        'title': 'Профиль',
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(user=self.request.user).order_by('-created')



