import time

import rest_framework.exceptions
from django.shortcuts import render

# Create your views here.
from django.db.models import Q

from models.models import FileModel,User,Organization
from . serializers import FileSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid
import oss2
import os
from tools.common import FILE_UPLOAD_CACHE_PATH

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
auth = oss2.Auth('LTAI5tNtrJxgmQ5pgAMjGoH2', 'BlKZ0n8As55Jqgju1RObVCOsaT1705')
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称。
bucket = oss2.Bucket(auth, 'oss-cn-hangzhou.aliyuncs.com', 'all-is-ready-file-storage')



class Upload(APIView):

    def post(self,request):
        tmp={}
        tmp['UID']=(request.user['UID'])
        tmp['Renewal']=int(time.time())
        orgID=request.data.get('OrgID')
        if int(orgID) !=-1:
            if not Organization.objects.filter(OrgID=orgID):
                raise rest_framework.exceptions.NotFound

        tmp['OrgID']=request.data.get('OrgID')
        tmp['FolderName']=request.data.get('FolderName')
        tmp['FileName'] = request.data.get('FileName')

        ser=FileSerializers(data=tmp)
        ser.is_valid(raise_exception=True)

        f = request.FILES.get('book')
        if not f:
            return Response({"no file detect"})

        oss_upload_path = 'userPDF/' + str(ser.data.get('UID')) + '/' + str(ser.data.get('FolderName')) + '/' +str(ser.data.get('FileName'))
        tmp_cache_path = os.path.join(FILE_UPLOAD_CACHE_PATH, f.name)


        #check repeat file
        check=FileModel.objects.filter(Q(UID__exact=ser.data.get('UID')),Q(FileName=ser.data.get('FileName')),Q(FoldName=ser.data.get('FolderName'))).first()
        if check:
            check.Renewal=int(time.time())
            check.save()
            # override file
            self.uploadFile(f,tmp_cache_path,oss_upload_path)
        else:
            ser.save()
            #upload to oss
            self.uploadFile(f, tmp_cache_path, oss_upload_path)


        return Response(ser.data,status=status.HTTP_200_OK)



    def uploadFile(self,FILE,TMP_PATH,OSS_PATH):
        try:
            with open(TMP_PATH, 'wb+') as fileobj:
                for chunk in FILE.chunks():
                    fileobj.write(chunk)
        except Exception as e:
            print(e)
            return Response({'result': "cache save failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            bucket.put_object_from_file(OSS_PATH, TMP_PATH)
        except Exception as e:
            print(e)
            return Response({'result', "oss upload failed"})


class Detail(ModelViewSet):

    @action(methods=['get'], detail=False, url_path="FoldList")
    def get_fold_list(self,request):
        UID=request.user['UID']
        data=FileModel.objects.filter(UID__exact=UID).values('FolderName').distinct().order_by('FolderName')
        return Response(data,status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path="FileList")
    def get_file_list(self,request):
        UID=request.user['UID']
        Folder=request.data.get('Folder')
        data=FileModel.objects.filter(Q(UID__exact=UID),Q(FolderName__exact=Folder)).order_by('FileName')
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path="OnlinePreview")
    def get_preview_url(self,request):
        FileID = request.data.get('FileID')
        UID = request.user['UID']
        data=FileModel.objects.filter(Q(UID=UID),Q(ID=FileID)).first()
        if not data:
            return Response({'result':'no such file'},status=status.HTTP_204_NO_CONTENT)

        obj_path = "userPDF/"+str(UID)+"/"+data.FolderName+"/"+data.FileName
        url = bucket.sign_url('GET', obj_path, 7200, slash_safe=True)
        return Response({'url':url},status=status.HTTP_200_OK)



