from json import loads

import pymorphy2 as pymorphy2
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class Text2SignView(View):
    def post(self, request):
        # Probably should do some catches
        if True:
            data = loads(request.body)
            print(data)
            sentence = data.get('message')
        else:
            sentence = "ехал грека через реку"
        morph = pymorphy2.MorphAnalyzer()
        res = []
        for word in sentence.split(' '):
            p = morph.parse(word)[0]
            res.append(p.normal_form)
        context = {
            'words': res
        }
        return JsonResponse(context)
