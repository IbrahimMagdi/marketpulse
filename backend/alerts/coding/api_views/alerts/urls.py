from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .code import *

urlpatterns = [
   path('create', create_api),
   path('list', list_api),
   path('details', details_api),
   path('update', update_api),
   path('delete', delete_api),
]

