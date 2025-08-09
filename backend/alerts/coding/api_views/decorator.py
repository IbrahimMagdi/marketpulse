from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.contrib.auth.models import AnonymousUser


def require_jwt(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        user = None
        try:
            user_auth_tuple = JWTAuthentication().authenticate(request)
            if user_auth_tuple is not None:
                user, _ = user_auth_tuple
        except (InvalidToken, AuthenticationFailed) as e:
            return Response(
                {"details": str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user or not user.is_authenticated:
            request.user = AnonymousUser()
            return Response(
                {"details": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        request.user = user
        return view_func(request, *args, **kwargs)

    return wrapped_view
