from django.contrib.auth import (
    logout as django_logout
)
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

from rest_framework import status
from rest_framework.response import Response

from rest_auth.views import LogoutView
from rest_framework.permissions import IsAuthenticated


class MultitokenLogoutView(LogoutView):
    permission_classes = [IsAuthenticated]

    def logout(self, request):
        request.user.auth_multitoken.delete()
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response({"detail": _("Successfully logged out.")}, status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False):
            from rest_framework_jwt.settings import api_settings as jwt_settings
            if jwt_settings.JWT_AUTH_COOKIE:
                response.delete_cookie(jwt_settings.JWT_AUTH_COOKIE)
        return response