import os
from django.urls import path
from .views import GetSign

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('', GetSign.as_view()),
]