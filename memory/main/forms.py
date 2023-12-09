from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django import forms
from .models import PostalLetterModel


class PostalLetterForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)

    class Meta:
        model = PostalLetterModel
        fields = '__all__'
        exclude = ['created']
        widgets = {
            'name_from': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'send_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
            }),
            'name_to': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True,
            }),
        }