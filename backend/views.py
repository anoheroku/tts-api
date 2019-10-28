from json import loads

import pymorphy2 as pymorphy2
from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.views import View


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
        signs = self.get_signs(words)
        context = {
            'message': sentence,
            'words': words,
            'signs': signs
        }
        return JsonResponse(context)

    @staticmethod
    def get_signs(words):
        assert words
        return 'Not yet'

    @staticmethod
    def get_words(sentence):
        morph = pymorphy2.MorphAnalyzer()
        result = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            result.append(p.normal_form)
        return result
