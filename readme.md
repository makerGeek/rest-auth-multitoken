# Rest Auth Multitoken

[django-rest-auth](https://github.com/Tivix/django-rest-auth) is a great package 
for authentication with django, however it lacks the possibility of allowing a user
 to have multiple auth tokens. Thus a user has a single token shared across all his
  clients, and when he logs out from one client he gets logged out of all his clients.

rest-auth-multitoken solves this problem by adding  multiple tokens support for a single user to django-rest-auth.

# Installation

install `rest-auth-multitoken`
```
> pip install rest-auth-multitoken
```

Then in django's `settings.py`:

add it to `INSTALLED_APPS`: 
```py
# settings.py
INSTALLED_APPS = [
    ...
    'rest_auth_multitoken',
    ...
]
```

add it to `REST_FRAMEWORK`'s  config:

```py
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_auth_multitoken.utils.MultiTokenAuthentication',
        ...
    ),
}

```

configure `django-rest-auth` to use `rest-auth-multitoken`:
```py
                                                          # settings.py
REST_AUTH_TOKEN_CREATOR = 'rest_auth_multitoken.utils.multitoken_create'
REST_AUTH_TOKEN_MODEL = 'rest_auth_multitoken.models.Token'
```

Finally include the new `LogoutView` in `urls.py`, just before `django-rest-auth`'s urls:

```py
# urls.py
from rest_auth_multitoken import MultitokenLogoutView


urlpatterns = [
    ...
    path('api/auth/logout/', MultitokenLogoutView.as_view()),
    path('api/auth/', include('rest_auth.urls')),
    ...
]
```

Now everytime a user logs in he'll get a new token, even if he's logged in from another client.