from django.db import models


class ServicesCategories(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    class_cat = models.CharField(
        max_length=20,
        blank=False,
        verbose_name='CSS класс для категории'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_categories():
        return ServicesCategories.objects.filter(is_active=True)

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'


class Services(models.Model):
    category = models.ForeignKey(
        ServicesCategories,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название услуги',
        blank=False,
    )
    description = models.TextField(
        verbose_name='Описание услуги',
        blank=False,
    )
    features = models.TextField(
        verbose_name='Особенности услуги',
        blank=False,
    )
    for_gender = models.CharField(
        max_length=100,
        verbose_name='Для кого',
        blank=False,
    )
    special_rate = models.TextField(
        verbose_name='Специальные условия для пользователей',
        blank=False,
    )
    vip = models.TextField(
        verbose_name='VIP условия',
        blank=False,
    )
    main_image = models.ImageField(
        upload_to='images/services',
        verbose_name='Главная картинка',
    )
    image_slider_1 = models.ImageField(
        upload_to='images/services',
        verbose_name='Картинка для слайдера 1',
    )
    image_slider_2 = models.ImageField(
        upload_to='images/services',
        verbose_name='Картинка для слайдера 2',
    )
    image_slider_3 = models.ImageField(
        upload_to='images/services',
        verbose_name='Картинка для слайдера 3',
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name='Стоимость',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.name} ({self.category})'

    @staticmethod
    def get_services():
        return Services.objects.filter(is_active=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
