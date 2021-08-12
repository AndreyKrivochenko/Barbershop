import json
import os

from django.core.management import BaseCommand

from mainapp.models import ClassForMainGallery, MainGallery

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
