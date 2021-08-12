from django.db import models


class ClassForMainGallery(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Имя'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс для галереи'
        verbose_name_plural = 'Классы для галереи'


class MainGallery(models.Model):
    class_obj = models.OneToOneField(
        ClassForMainGallery,
        primary_key=True,
        on_delete=models.PROTECT,
        verbose_name='Класс для галереи',
    )
    image = models.ImageField(
        upload_to='home-page/projects',
        blank=True,
        verbose_name='Изображение',
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Название',
    )
    short_desc = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Описание',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
