from json import loads
import pymorphy2 as pymorphy2
from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.views import View
from storageapp.models import Sign
from django.contrib.sites.shortcuts import get_current_site
from .models import Sign


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
        for word in words:
            try:
                word_url = Sign.objects.get(normal_form=word).image.url
            except:
                word_url = '/media/normal_form_img/poster_none.png'
            result.append(get_current_site(request).domain + word_url)
        return result

    @staticmethod
    def get_words(sentence):
        morph = pymorphy2.MorphAnalyzer()
        result = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            result.append(p.normal_form)
        return result
