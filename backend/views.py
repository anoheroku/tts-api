from json import loads, load

import pymorphy2 as pymorphy2
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


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
        morph = pymorphy2.MorphAnalyzer()
        res = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            res.append(p.normal_form)
        context = {
            'message': sentence,
            'words': res,
            'signs': self.get_signs(res)
        }
        return JsonResponse(context)

    @staticmethod
    def get_signs(words):
        assert words
        return 'Not yet'
