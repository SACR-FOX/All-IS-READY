import json
import time
from django.db.models import Q

from models.models import Organization,User,OrgTask,TaskAck
from . serializers import OrganizationSerializer,TaskSerializer,AckSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid

class OrgAction(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = "OrgID"

    @action(methods=['put'],detail=True,url_path="Modify")
    def Modify(self,request,OrgID):
        Org=Organization.objects.get(OrgID=OrgID)
        ser=OrganizationSerializer(instance=Org,data=request.data,partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class OrgTaskAction(ModelViewSet):
    #增删改
    queryset = OrgTask.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "TaskID"


    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, TaskID):
        Tsk = OrgTask.objects.get(TaskID=TaskID)
        ser = TaskSerializer(instance=Tsk, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class OrgTaskAll(APIView):

    def get(self,request):
        OrgID = request.data.get("OrgID")
        Tsk = OrgTask.objects.filter(OrgID=OrgID)
        ser = TaskSerializer(instance=Tsk, many=True)
        return Response(ser.data)


class ACK(APIView):

    def post(self,request):
        UID=request.data.get("UID")
        TaskID=request.data.get("TaskID")
        Tsk = OrgTask.objects.get(TaskID=TaskID)
        Usr=User.objects.get(UID=UID)
        dataFinish= {
            "TaskID": TaskID,
            "Status": True
        }
        dataFailed={
            "result":"sanction denied"
        }
        if Usr.OrgID != Tsk.OrgID:
            return Response(dataFailed,status=status.HTTP_403_FORBIDDEN)

        if TaskAck.objects.filter(Q(UID=UID),Q(TaskID=TaskID)).exists():

            return Response(dataFinish,status=status.HTTP_200_OK)

        else:
            Tsk.AckCount+=1
            Tsk.save()
            TaskAck.objects.create(UID=UID,TaskID=TaskID)
            return Response(dataFinish, status=status.HTTP_200_OK)

    def get(self,request):
        UID = request.data.get("UID")
        TaskID = request.data.get("TaskID")
        if TaskAck.objects.filter(Q(UID=UID), Q(TaskID=TaskID)).exists():
            data = {
                "TaskID": TaskID,
                "Status": True
            }
            return Response(data,status=status.HTTP_200_OK)

        else:
            data = {
                "TaskID": TaskID,
                "Status": False
            }
            return Response(data,status=status.HTTP_200_OK)