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
        upload_to='images/home-page/projects',
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


class MainSlider(models.Model):
    image = models.ImageField(
        upload_to='images/slider/',
        blank=False,
        verbose_name='Изображение',
    )
    description = models.TextField(
        max_length=200,
        blank=False,
        verbose_name='Описание',
    )
    url = models.URLField(
        verbose_name='Ссылка',
        blank=False,
        default='#',
    )
    button_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        verbose_name='Название кнопки'
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'
