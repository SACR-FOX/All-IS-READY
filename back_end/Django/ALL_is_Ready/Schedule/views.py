import json
import time

import requests
from django.db.models import Q

from models.models import Schedule,User
from . serializers import ScheduleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid


class Schedule_byday(APIView):

    def get(self,request):
        UID = request.user['UID']
        # weekNum=datetime.today().isoweekday()
        day=request.query_params.get('Day')
        datalist=Schedule.objects.filter(Q(Day=day),Q(UID__exact=UID)).order_by("DurationStart")
        Switcher = switcher()

        result={}
        content=[]
        for i in datalist:
            Dict={}
            Dict['ScheduleID'] = i.ScheduleID
            Dict["CurName"]=i.CurName
            Dict["Location"]=i.Location
            Dict["Tag"]=i.Tag
            Dict["Start"]=Switcher.sec2hm(i.DurationStart)
            Dict["End"] =Switcher.sec2hm(i.DurationEnd)

            content.append(Dict)

        result['content']=content
        result['result']='ok'
        return Response(result,status=status.HTTP_200_OK)

class Schedule_next(APIView):

    def get(self, request):
        UID=request.user['UID']
        token =  "ScheduleNext"+str(UID)

        try:
            data = cache.get(token)
            if data:
                # print("hit")
                return Response(json.loads(data),status=status.HTTP_200_OK)

        except Exception as e:
            print(e)


        weekNum = datetime.today().isoweekday()
        Switcher = switcher()
        match= Schedule.objects.filter(Q(Day=weekNum), Q(UID__exact=UID),Q(DurationEnd__gte=Switcher.secFrom0())).order_by("DurationStart").first()
        if not match:
            return Response({"result: Empty"},status=status.HTTP_200_OK)
        Dict = {}
        Dict["CurName"] = match.CurName
        Dict["Location"] = match.Location
        Dict["Tag"] = match.Tag
        Dict["Start"]=match.DurationStart
        Dict["End"]=match.DurationEnd

        try:
            cache.set(token,json.dumps(Dict),Switcher.due(match.DurationEnd))
        except Exception as e:
            print(e)
            return Response({"result":"internal error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(Dict,status=status.HTTP_200_OK)


class ScheduleAction(ModelViewSet):
 #增删改
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "ScheduleID"

    @action(methods=['put'],detail=True,url_path="Modify")
    def Modify(self,request,ScheduleID):
        sc=Schedule.objects.get(ScheduleID__exact=ScheduleID)
        ser=ScheduleSerializer(instance=sc,data=request.data,partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data,status=status.HTTP_200_OK)



class GroupImport(APIView):  #按组织批量导入

    def post(self,request):

        orgID = request.data.get("OrgID")
        UID = request.user['UID']
        try:
            sc=Schedule.objects.filter(Q(OrgID__exact=orgID),Q(UID__exact=-1))
            if sc:
                for i in sc:

                    check=Schedule.objects.filter(Q(UUID__exact=i.UUID),Q(UID__exact=UID))
                    if check.exists():
                        # print("exists")
                        pass
                    else:
                        Schedule.objects.create(UID=UID,OrgID=orgID,DurationStart=i.DurationStart,
                                                DurationEnd = i.DurationEnd,Day=i.Day,CurName=i.CurName,
                                                Tag=i.Tag,UUID=i.UUID,Location=i.Location
                                                )

        except Exception as e:
            print(e)
            return Response({'result':'internal error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'result':'ok'},status=status.HTTP_200_OK)


