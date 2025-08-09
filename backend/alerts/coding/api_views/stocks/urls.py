from django.urls import path, include
from .code import *

urlpatterns = [
   path('list', list_api),
   path('details', details_api),
]

