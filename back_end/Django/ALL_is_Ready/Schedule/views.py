import json
import time

from django.db.models import Q

from models.models import Schedule,User
from . serializers import ScheduleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.scheduleTool import switcher
from django.core.cache import cache



class Schedule_today(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "UID"

    @action(methods=['get'],detail=True,url_path="today")
    def Today(self,request,UID):


        weekNum=datetime.today().isoweekday()
        self.queryset=self.queryset.filter(Q(Day=weekNum),Q(UID__exact=UID)).order_by("DurationStart")
        Switcher = switcher()
        data=[]
        for i in self.queryset:
            Dict={}
            Dict["CurName"]=i.CurName
            Dict["Location"]=i.Location
            Dict["Tag"]=i.Tag
            Dict["Day"]=i.Day
            Dict["Start"]=Switcher.sec2hm(i.DurationStart)
            Dict["End"] =Switcher.sec2hm(i.DurationEnd)
            data.append(Dict)

        return Response(data)

class Schedule_next(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "UID"

    @action(methods=['get'], detail=True, url_path="next")
    def Next(self, request, UID):
        token =  "ScheduleNext"+str(UID)
        print(token)

        try:
            data = json.load(cache.get(token))
            print(data)
            if data:
                return Response(data)
        except Exception as e:
            print(e)


        weekNum = datetime.today().isoweekday()
        Switcher = switcher()
        self.queryset = self.queryset.filter(Q(Day=weekNum), Q(UID__exact=UID),Q(DurationEnd__gte=Switcher.secFrom0())).order_by("DurationStart")
        data = []
        Dict = {}
        Dict["CurName"] = self.queryset.first().CurName
        Dict["Location"] = self.queryset.first().Location
        Dict["Tag"] = self.queryset.first().Tag
        data.append(Dict)
        try:
            cache.set(token,json.dumps(data),Switcher.due(self.queryset.first().DurationEnd))
        except Exception as e:
            print(e)

        return Response(data)


class ScheduleAction(ModelViewSet):
 #增删查
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "ScheduleID"

class ScheduleModify(ModelViewSet):
    #改

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "ScheduleID"

    @action(methods=['put'],detail=True,url_path="Modify")
    def Modify(self,request,ScheduleID):
        sc=Schedule.objects.get(ScheduleID__exact=ScheduleID)
        ser=ScheduleSerializer(instance=sc,data=request.data,partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class GroupImport(APIView):  #按组织批量导入

    def post(self,request):

        orgID = request.data.get("OrgID")
        UID = request.data.get("UID")
        print(orgID)
        try:
            sc=Schedule.objects.filter(Q(OrgID__exact=orgID),Q(UID__exact=-1))
            for i in sc:
                Schedule.objects.create(UID=UID,OrgID=orgID,DurationStart=i.DurationStart,
                                        DurationEnd = i.DurationEnd,Repeat=i.Repeat,CurName=i.CurName,
                                        Tag=i.Tag
                                        )

        except Exception as e:
            print(e)
            return Response("{'result':'err'}",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("{'result':'ok'}",status=status.HTTP_200_OK)


