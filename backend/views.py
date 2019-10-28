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
            data = load(request.body)
        if True:
            print(data)
            sentence = data.get('message')
        morph = pymorphy2.MorphAnalyzer()
        res = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            res.append(p.normal_form)
        context = {
            'words': res
        }
        return JsonResponse(context)
