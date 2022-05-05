from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from jwt import exceptions
from rest_framework import request

salt="AllIsReadyUserProfile"

class JWT_verify(BaseAuthentication):
    def authenticate(self, request):
        token=request.query_params.get('token')
        try:
            info=jwt.decode(token,salt,algorithms=["HS256"])
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'code':1003,'error':"token was expired"})
        except jwt.DecodeError:
            raise AuthenticationFailed({'code':1003,'error':"internal error"})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({'code':1003,'error':"invalid token value"})

        return (info,token)