from django.db import models


class AboutUs(models.Model):
    image = models.ImageField(
        upload_to='images/',
        blank=False,
        verbose_name='Изображение',
    )
    head_1 = models.CharField(
        max_length=70,
        blank=False,
        null=False,
        verbose_name='Заголовок 1'
    )
    text_1 = models.TextField(
        blank=False,
        null=False,
        verbose_name='Текст для 1-го заголовка'
    )
    head_2 = models.CharField(
        max_length=70,
        blank=False,
        null=False,
        verbose_name='Заголовок 2'
    )
    text_2 = models.TextField(
        blank=False,
        null=False,
        verbose_name='Текст для 2-го заголовка'
    )
    head_3 = models.CharField(
        max_length=70,
        blank=False,
        null=False,
        verbose_name='Заголовок 3'
    )
    text_3 = models.TextField(
        blank=False,
        null=False,
        verbose_name='Текст для 1-го заголовка'
    )

    def __str__(self):
        return 'Аккордеон'

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
