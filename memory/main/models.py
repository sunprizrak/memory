from django.contrib.auth import get_user_model
from django.db import models


class PostalLetterModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    name_from = models.CharField(verbose_name='От кого', max_length=150, blank=True)
    send_date = models.DateField(verbose_name='Дата отправки письма')
    name_to = models.CharField(verbose_name='Кому')
    address = models.CharField(verbose_name='Адрес получателя')
    email = models.EmailField(verbose_name='Email отправителя', max_length=254, blank=True)
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return f'Письмо для {self.name_to}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'