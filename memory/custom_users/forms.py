from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm


class RegistrationUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'required': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'required': True})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'required': True})


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'required': True}))