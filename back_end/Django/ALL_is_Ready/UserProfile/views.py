from django.db.models import Q
from rest_framework.generics import GenericAPIView
from models.models import User
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from tools.verify import JWT_verify
import tools.deriveToken as tokenCreator
from rest_framework.views import APIView
import rest_framework.status

class UserDetail (ModelViewSet): #用户属性方法 查询/修改信息
    authentication_classes = [JWT_verify,]
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


class UserLogin(APIView):  #注册/登录/退出
    #取消验证
    authentication_classes = []
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')


        usr=User.objects.filter(Q(Uname=username),Q(Passwd=password)).first()
        if not usr:
            return Response({'result':'用户名或密码错误','code':status.HTTP_401_UNAUTHORIZED})

        token=tokenCreator.create(usr,180)
        return Response({'result':'check passed','code':status.HTTP_200_OK,'token':token})


