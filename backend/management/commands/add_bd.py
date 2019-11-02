from django.core.management.base import BaseCommand
from backend.models import Sign
from shutil import copy2, move

from json import load
from os import path, mkdir
from django.conf import settings

JSON_PATH = settings.JSON_PATH
IMAGE_SIGN_PATH = settings.IMAGE_SIGN_PATH
if not path.exists(IMAGE_SIGN_PATH):
    mkdir(path.join(settings.MEDIA, IMAGE_SIGN_PATH))


def load_from_json():
    with open(path.join(JSON_PATH, 'data.json'), 'r', encoding="utf-8") as file:
        return load(file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        signs = load_from_json()

        for sign in signs:
            if 'sources' in sign['file']:
                file_url = sign['file'].replace('sources', IMAGE_SIGN_PATH)
                # Если файлы будем удалять после переноса
                # move(sign['file'], path.join(settings.MEDIA, file_url))
                copy2(sign['file'], path.join(settings.MEDIA, file_url))
                sign['file'] = file_url
            new_sign = Sign(**sign)
            new_sign.save()
