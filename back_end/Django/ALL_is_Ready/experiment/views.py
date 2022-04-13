from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class test(APIView):

    def post(self,request):
        days=request.data.get('days').split(",")
        print(days[3])
        return Response("ok")

    def get(self,request):
        print(request.user['Uname'])
        return Response({"result":"ok"})