from rest_framework.generics import GenericAPIView
from models.models import User
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.response import Response

class UserAPI(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)