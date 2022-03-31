from rest_framework.generics import GenericAPIView
from models.models import User
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView

class UserAPI(CreateAPIView,RetrieveAPIView,UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field="UID"

