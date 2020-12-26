from rest_framework.authentication import TokenAuthentication

from rest_auth_multitoken.rest_auth_multitoken.models import Token


def multitoken_create(token_model, user, serializer):
    token = token_model(user=user)
    token.save()
    return token


class MultiTokenAuthentication(TokenAuthentication):
    model = Token

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        try:
            user.auth_multitoken = Token.objects.get(key=key)
        except:
            user.auth_multitoken = None
        return user, token