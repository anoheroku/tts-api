from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from backend.views import Text2SignView

app_name = 'api'


urlpatterns = [
    path('text2sign', csrf_exempt(Text2SignView.as_view()), name='text2sign'),
    # path('sign2text', Sign2TextView.as_view(), name='sign2text')
]
