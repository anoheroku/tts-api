from django.core.management.base import BaseCommand
from backend.models import Sign
import shutil

import json
import os

JSON_PATH = 'backend/json'
IMAGE_SIGN_PATH = 'normal_form_img'
if not os.path.exists(IMAGE_SIGN_PATH):
    os.mkdir(IMAGE_SIGN_PATH)


def load_from_json():
    with open(os.path.join(JSON_PATH, 'data.json'), 'r', encoding="utf-8") as file:
        return json.load(file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        signs = load_from_json()

        for sign in signs:
            if 'sources' in sign['file']:
                file_url = sign['file'].replace('sources', IMAGE_SIGN_PATH)
                # Если файлы будем удалять после переноса
                # shutil.move(sign['file'], file_url)
                shutil.copy2(sign['file'], file_url)
                sign['file'] = file_url
            new_sign = Sign(**sign)
            new_sign.save()


