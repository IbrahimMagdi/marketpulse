from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .code import *

urlpatterns = [
   path('sign-up', signup_api),
   path('sign-in', signin_api),
   path('token/refresh', TokenRefreshView.as_view()),
]

