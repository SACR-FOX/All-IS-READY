from rest_framework.generics import GenericAPIView
from models.models import User
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class UserDetail (ModelViewSet): #用户属性方法 查询/修改信息
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field="UID"

    @action(methods=['put'],detail=True,url_path="InfoModify")
    def InfoModify(self,request,UID):
        user=self.queryset.get(UID__exact=UID)
        ser=UserSerializers(instance=user,data=request.data,partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data={"result":"ok"})


class UserAction(ModelViewSet):  #注册/登录/退出
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = "UID"
