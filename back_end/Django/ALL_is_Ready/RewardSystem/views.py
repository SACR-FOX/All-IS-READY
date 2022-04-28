
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
        durations=float(request.data.get('Durations'))
        item=request.data.get('ItemName')

        #choose
        if item == 'ToDoList':
            CommonTools.addEXP(usr,5)
            # CommonTools.EXP2Rank(usr.EXP)

        if item == 'Timer':
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



