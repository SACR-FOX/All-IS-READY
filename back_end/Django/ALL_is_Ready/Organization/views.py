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
from tools import common as CommonTools
from . pagination import OrgTaskNumberPagination
from django.core.paginator import Paginator
sw=switcher()

class OrgAction(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = "OrgID"

    @action(methods=['put'],detail=True,url_path="Modify")
    def Modify(self,request,OrgID):
        Org=Organization.objects.get(OrgID=OrgID)
        if Org.MonitorID!=request.user['UID']:
            return Response({"result":"permission denied"},status=status.HTTP_403_FORBIDDEN)
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
        if Tsk.Creator!=request.user['Uname']:
            return Response({"result":"permission denied"},status=status.HTTP_403_FORBIDDEN)
        ser = TaskSerializer(instance=Tsk, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class OrgInfo(APIView):
    def get(self,request):
        OrgID=request.query_params.get('OrgID')
        Org=Organization.objects.filter(OrgID=OrgID).first()
        if Org:
            dict={}
            usr=User.objects.filter(UID__exact=Org.MonitorID).first()
            aggregate=User.objects.filter(OrgID=OrgID).count()
            dict['Monitor']=usr.Uname
            dict['aggregate']=aggregate
            dict['OrgName']=Org.OrgName
            dict['OrgID']=Org.OrgID
            dict['Description']=Org.Description
            return Response(dict,status=status.HTTP_200_OK)
        else:
            return Response({"result":"empty"},status=status.HTTP_200_OK)
class OrgTaskAll(APIView):

    def get(self,request):
        OrgID = request.user['OrgID']
        TaskLisk=OrgTask.objects.filter(OrgID=OrgID)
        page = request.query_params.get("page")
        if not page:
            page = 1
        else:
            page = int(page)


        result={}
        dataList=[]
        #check


        paginator = Paginator(TaskLisk,12)
        Page=paginator.page(page)
        if Page.has_next():
            result['next'] = True
        else:
            result['next'] = False
        if Page.has_previous():
            result['previous'] = True
        else:
            result['previous'] = False
        result['count'] = paginator.count

        for i in Page.object_list:
            item = {}
            item['TaskID'] = i.TaskID
            item['TaskName'] = i.TaskName
            if sw.ifPass(i.TimeDue):
                i.Status = False
                i.save()
                item['Status'] = i.Status
            else:
                item['Status'] = i.Status

            # item['TimeStart'] = i.TimeStart
            item['TimeDue'] = sw.stamp2str(i.TimeDue)
            # item['Description'] = i.Description
            # item['Creator'] = i.Creator
            # item['AckCount'] = i.AckCount
            # item['CID'] = i.CID
            dataList.append(item)

        result['data']=dataList
        return Response(result,status=status.HTTP_200_OK)

class ACK(APIView):

    def post(self,request):
        UID=request.user['UID']
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
            #检查任务截止时间
            now = int(time.time())
            if now > Tsk.TimeDue:
                if Tsk.Status:
                    Tsk.Status=False
                    Tsk.save()
                return Response({"result": "Task Due"}, status=status.HTTP_403_FORBIDDEN)

            Tsk.AckCount+=1
            Tsk.save()
            TaskAck.objects.create(UID=UID,TaskID=TaskID)
            CommonTools.addEXP(Usr, 5)
            # CommonTools.EXP2Rank(Usr.EXP)
            return Response(dataFinish, status=status.HTTP_200_OK)

    def get(self,request):
        UID = request.user['UID']
        TaskID = request.query_params.get("TaskID")
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