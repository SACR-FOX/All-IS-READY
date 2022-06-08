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
from tools import common

class UserDetail (ModelViewSet): #用户属性方法 查询/修改信息
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field="UID"


    @action(methods=['put'],url_path="InfoModify",detail=False)
    def InfoModify(self,request):
        UID=request.user['UID']
        user=self.queryset.get(UID__exact=UID)
        ser=UserSerializers(instance=user,data=request.data,partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data,status=status.HTTP_200_OK)

class UserRegister(APIView):

    authentication_classes = []

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            header = request.FILES.get('header')
        except Exception as e:

            header = common.HOST_PREFIX + "/static/img/header_default.png"

        if not header:
            header=common.HOST_PREFIX+"/static/img/header_default.png"

        if not User.objects.filter(Uname=username):
            try:
                User.objects.create(Uname=username,Passwd=password,Header=header,Rank=1,Accumulation=0,EXP=0)
            except Exception as e:
                print(e)
            return Response({"result":"ok"},status=status.HTTP_201_CREATED)

        else:
            return Response({"result": "username already exist"}, status=status.HTTP_403_FORBIDDEN)



class UserLogin(APIView):  #登录
    #取消验证
    authentication_classes = []
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')


        usr=User.objects.filter(Q(Uname=username),Q(Passwd=password)).first()
        if not usr:
            return Response({'result':'用户名或密码错误','code':status.HTTP_401_UNAUTHORIZED},status=status.HTTP_401_UNAUTHORIZED)

        token=tokenCreator.create(usr,1440)

        return Response({'result':'check passed','code':status.HTTP_200_OK,'token':token,'UID':usr.UID,'OrgID':usr.OrgID},status=status.HTTP_200_OK)


# class Rank(APIView):
#
#     def get(self,request):
#         OrgID=request.user['OrgID']
#         try:
#             usrs=User.objects.filter(OrgID=OrgID).order_by('-Accumulation','-EXP')[:10]
#             date={}
#             date['result']="ok"
#             usrList=[]
#             for u in usrs:
#                 item={}
#                 item['Uname']=u.Uname
#                 item['header']=common.HOST_PREFIX+u.Header.url
#                 item['Rank']=u.Rank
#                 item['Accumulation']=u.Accumulation
#                 usrList.append(item)
#
#             date['data']=usrList
#             return Response(date,status=status.HTTP_200_OK)
#
#         except Exception as e:
#             print(e)
#             return Response({"result":"internal error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


