import json
import pymorphy2 as pymorphy2

from json import loads
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.views import View
from backend.models import Sign


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
        words_url = self.get_words_url(words, request)
        signs = self.get_signs(words)
        context = {
            'message': sentence,
            'words': words,
            'words_url': words_url,
            'signs': signs
        }
        return JsonResponse(context)

    @staticmethod
    def get_signs(words):
        assert words
        return ['Not', 'yet']

    @staticmethod
    def get_words(sentence):
        morph = pymorphy2.MorphAnalyzer()
        result = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            result.append(p.normal_form)
        return result

    @staticmethod
    def get_words_url(words, request):
        result = []
        for word in words:
            try:
                word_url = Sign.objects.get(normal_form=word).image.url
            except:
                word_url = 'media/normal_form_img/poster_none.png'
            result.append(get_current_site(request).domain + word_url)
        return result
    
    
# class GetSign(View):
#
#     def get(self, request, *args, **kwargs):
#         json_data = json.loads(request.body.decode("utf-8"))
#         morph = pymorphy2.MorphAnalyzer()
#         data = {}
#         for key, value in json_data.items():
#             normal_form = morph.parse(value)[0].normal_form
#             try:
#                 normal_form_url = Sign.objects.get(normal_form=normal_form).image.url
#             except:
#                 normal_form_url = Sign.objects.get(normal_form='none').image.url
#             data[key] = get_current_site(request).domain + normal_form_url
#         dump = json.dumps(data)
#         return HttpResponse(dump, content_type='application/json')
