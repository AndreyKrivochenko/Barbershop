# Generated by Django 3.2.6 on 2021-08-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('features', models.TextField(verbose_name='Особенности услуги')),
                ('for_gender', models.CharField(max_length=100, verbose_name='Для кого')),
                ('special_rate', models.TextField(verbose_name='Специальные условия для пользователей')),
                ('vip', models.TextField(verbose_name='VIP условия')),
                ('main_image', models.ImageField(upload_to='images/services', verbose_name='Главная картинка')),
                ('image_slider_1', models.ImageField(upload_to='images/services', verbose_name='Картинка для слайдера 1')),
                ('image_slider_2', models.ImageField(upload_to='images/services', verbose_name='Картинка для слайдера 2')),
                ('image_slider_3', models.ImageField(upload_to='images/services', verbose_name='Картинка для слайдера 3')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesapp.servicescategories')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
