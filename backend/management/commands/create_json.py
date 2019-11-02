from django.core.management.base import BaseCommand
from json import dump
from os import path, mkdir, listdir
from shutil import copy2, move
from django.conf import settings


TRANS = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'x', 'ы': 'y', 'ь': 'xx', 'э': 'e', 'ю': 'iu', 'я': 'ia', 'ё': 'e'}

JSON_PATH = settings.JSON_PATH
if not path.exists(JSON_PATH):
    mkdir(JSON_PATH)


def translit(name):
    result = ''
    for s in name:
        result += TRANS[s]
    return result


def create_from_json(data):
    with open(path.join(JSON_PATH, 'data.json'), 'w', encoding="utf-8") as f:
        dump(data, f, ensure_ascii=False)


class Command(BaseCommand):
    def handle(self, *args, **options):
        path_old = path.join('sources', 'images_cyrillic_name')
        path_new = "sources"
        file_names = listdir(path=path_old)
        data = []
        
        for file in file_names:
            word = {}
            normal_form = path.splitext(file)[0]
            file_name = translit(normal_form)
            url = f'{path_new}/{file_name + path.splitext(file)[1]}'
            # если файлы удалять будем при переносе
            # move(os.path.join(path_old, file), os.path.join(path_new, path.join(file_name, path.splitext(file)[1])))
            copy2(path.join(path_old, file), path.join(path_new, path.join(file_name, path.splitext(file)[1])))
            word['normal_form'] = normal_form
            word['file'] = url
            data.append(word)

        with open(path.join(JSON_PATH, 'data.json'), 'w', encoding="utf-8") as f:
            dump(data, f, ensure_ascii=False)
            print('ok')
