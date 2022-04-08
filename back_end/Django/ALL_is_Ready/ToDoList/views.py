import json
import time

from django.db.models import Q

from models.models import ToDoList,User
from . serializers import ToDoListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid

Switcher=switcher()

class ListAction(ModelViewSet):# 增删改

    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    lookup_field = "ID"

    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, ID):
        TDL = ToDoList.objects.get(ID__exact=ID)
        ser = ToDoListSerializer(instance=TDL, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)



class ListAll(APIView):

    def get(self,request):
        UID = request.data.get("UID")
        data=ToDoList.objects.filter(UID__exact=UID).order_by("Time")
        ser=ToDoListSerializer(instance=data,many=True)

        return Response(ser.data)

class ListToday(APIView):

    def get(self,request):
        duration=[Switcher.daySec(),Switcher.daySec()+86400]
        UID = request.data.get("UID")
        data=ToDoList.objects.filter(Q(UID__exact=UID),Q(Time__gte=duration[0]),Q(Time__lte=duration[1])).order_by("Time")
        ser=ToDoListSerializer(instance=data,many=True)

        return Response(ser.data)

class GroupImport(APIView):  #按组织批量导入

    def post(self,request):

        orgID = request.data.get("OrgID")
        UID = request.data.get("UID")
        try:
            L=ToDoList.objects.filter(Q(OrgID__exact=orgID),Q(UID__exact=-1))
            for i in L:

                check=ToDoList.objects.filter(Q(UUID__exact=i.UUID),Q(UID__exact=UID))
                if check.exists():
                    print("exists")
                else:
                    ToDoList.objects.create(UID=UID,OrgID=orgID,ItemName=i.ItemName,Time=i.Time,
                                            Status=i.Status,Tag=i.Tag,UUID=i.UUID
                                            )

        except Exception as e:
            print(e)
            return Response("{'result':'err'}",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("{'result':'ok'}",status=status.HTTP_200_OK)

class ItemStatistics(APIView):
    def get(self,request):
        duration = [Switcher.daySec(), Switcher.daySec() + 86400]
        UID = request.data.get("UID")
        today=ToDoList.objects.filter(Q(UID__exact=UID),Q(Time__gte=duration[0]),Q(Time__lte=duration[1]),Q(Status=False)).count()
        all_in_plan=ToDoList.objects.filter(Q(UID__exact=UID),Q(Status=False)).count()
        finished=ToDoList.objects.filter(Q(UID__exact=UID),Q(Status=True)).count()
        data={
            "today":today,
            "all_in_plan":all_in_plan,
            "finished":finished
        }
        return Response(data,status=status.HTTP_200_OK)
