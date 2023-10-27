from django.db import models


class MemorandumModel(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150, blank=True)
    send_date = models.DateTimeField(verbose_name='Дата отправки')
    email = models.EmailField(verbose_name='Email получателя', max_length=254)
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return f'Записка для {self.email}'

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'
