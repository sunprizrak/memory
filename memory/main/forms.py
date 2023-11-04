from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from .models import PostalLetterModel


class PostalLetterForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)

    class Meta:
        model = PostalLetterModel
        fields = '__all__'
        exclude = ['created']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'send_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'required': True,
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True,
            }),
        }