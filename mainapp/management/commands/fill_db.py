import json
import os

from django.core.management import BaseCommand

from mainapp.models import ClassForMainGallery, MainGallery, MainSlider, AboutUs
from servicesapp.models import ServicesCategories, Services

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        class_for_gallery = load_from_json('class_for_gallery')

        ClassForMainGallery.objects.all().delete()
        for _class in class_for_gallery:
            new_class = ClassForMainGallery(**_class)
            new_class.save()

        gallery = load_from_json('gallery')

        MainGallery.objects.all().delete()
        for gal in gallery:
            gal_class = gal['class_obj']
            class_obj = ClassForMainGallery.objects.get(name=gal_class)
            gal['class_obj'] = class_obj
            new_gal = MainGallery(**gal)
            new_gal.save()

        slider = load_from_json('slider')

        MainSlider.objects.all().delete()
        for slide in slider:
            new_slide = MainSlider(**slide)
            new_slide.save()

        about = load_from_json('about')
        AboutUs.objects.all().delete()
        new_about = AboutUs(**about)
        new_about.save()

        # Создаём категории для услуг
        services_categories = load_from_json('services_categories')
        ServicesCategories.objects.all().delete()
        for category in services_categories:
            new_category = ServicesCategories(**category)
            new_category.save()

        # Создаем услуги
        services = load_from_json('services')
        Services.objects.all().delete()
        for service in services:
            service_cat = service['category']
            cat_obj = ServicesCategories.objects.get(name=service_cat)
            service['category'] = cat_obj
            new_service = Services(**service)
            new_service.save()
