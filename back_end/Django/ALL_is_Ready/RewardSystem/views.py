
import time
from django.db.models import Q
from models.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.core.cache import cache
import uuid

from tools import common as CommonTools

class Reward(APIView):
    def post(self,request):
        usr=User.objects.get(UID=request.user['UID'])

        item=request.data.get('ItemName')

        #choose
        # if item == 'ToDoList':
        #     CommonTools.addEXP(usr,5)
        #     # CommonTools.EXP2Rank(usr.EXP)

        if item == 'Timer':
            try:
                durations = float(request.data.get('Durations'))
            except Exception as e:
                print(e)
                return Response({'result':'expect Durations'},status=status.HTTP_400_BAD_REQUEST)
            usr.Accumulation+=int(durations)
            usr.save()
            CommonTools.addEXP(usr,int(durations*10/3600))

        #return
        info={}
        info['UID']=usr.UID
        info['Uname']=usr.Uname
        info['Rank']=usr.Rank
        info['EXP']=usr.EXP
        info['Accumulation']=usr.Accumulation

        return Response(info,status=status.HTTP_200_OK)


class Situation(APIView):

    def get(self,request):
        usr=User.objects.get(UID=request.user['UID'])
        OrgUserList=User.objects.filter(OrgID=usr.OrgID).order_by("-Accumulation")
        print(OrgUserList.count())
        OrgRank=0
        for index,i in enumerate(OrgUserList):
            if i.UID == usr.UID:
                print(index)
                OrgRank=index
                print(index)
        return Response("Ok")



class Rank(APIView):

    def get(self,request):
        OrgID=request.user['OrgID']
        try:
            usrs=User.objects.filter(OrgID=OrgID).order_by('-Accumulation','-EXP')[:10]
            date={}
            date['result']="ok"
            usrList=[]
            for u in usrs:
                item={}
                item['Uname']=u.Uname
                item['header']=CommonTools.HOST_PREFIX+u.Header.url
                item['Rank']=u.Rank
                item['Accumulation']=u.Accumulation
                usrList.append(item)

            date['data']=usrList
            return Response(date,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"result":"internal error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




