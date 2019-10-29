from django.views.generic.base import View
import json
from django.http import HttpResponse
import pymorphy2
from storageapp.models import Sign
from django.contrib.sites.shortcuts import get_current_site


class GetSign(View):

    def get(self, request, *args, **kwargs):
        json_data = json.loads(request.body.decode("utf-8"))
        morph = pymorphy2.MorphAnalyzer()
        data = {}
        for key, value in json_data.items():
            normal_form = morph.parse(value)[0].normal_form
            try:
                normal_form_url = Sign.objects.get(normal_form=normal_form).image.url
            except:
                normal_form_url = Sign.objects.get(normal_form='none').image.url
            data[key] = get_current_site(request).domain + normal_form_url
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')
