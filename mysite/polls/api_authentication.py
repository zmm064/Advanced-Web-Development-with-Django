from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import authentication
from rest_framework import exceptions


class AdminOnlyAuth(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            username = request.query_params.get('username')
            password = request.query_params.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                raise exceptions.AuthenticationFailed('No such user!')
            return(user, None)
        except:
            raise exceptions.AuthenticationFailed('No such user!')
