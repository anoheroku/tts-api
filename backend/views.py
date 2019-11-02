from json import loads
import pymorphy2 as pymorphy2
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from .models import Sign
from django.conf import settings


class MainView(View):
    def get(self, request):
        return HttpResponse("Hello guest! Translate the sign API works")


class Text2SignView(View):
    def post(self, request):
        # Probably should do some catches
        try:
            data = loads(request.body)
        except TypeError:
            string = request.body.decode(encoding='utf-8')
            data = loads(string, encoding='utf-8')
        if True:
            print(data)
            sentence = data.get('message')

        words = self.get_words(sentence)
        signs = self.get_signs(words, request)
        context = {
            'message': sentence,
            'words': words,
            'signs': signs
        }
        return JsonResponse(context)

    @staticmethod
    def get_signs(words, request):
        result = []
        # Не стали делать - одним запросом получить сразу словарь
        # что бы не менять модель Sign ( поле normal_form не стали делать уникальным)
        # normal_form_image = Sign.objects.in_bulk(words, field_name='normal_form')
        queryset = Sign.objects.filter(normal_form__in=words).values_list('normal_form', 'file')
        normal_form_image = dict(queryset)
        for word in words:
            if normal_form_image.get(word):
                result.append(get_current_site(request).domain + settings.MEDIA_URL + normal_form_image.get(word))
            else:
                result.append(get_current_site(request).domain + settings.STATIC_URL + 'img/poster_none.png')
        return result

    @staticmethod
    def get_words(sentence):
        morph = pymorphy2.MorphAnalyzer()
        result = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            result.append(p.normal_form)
        return result
