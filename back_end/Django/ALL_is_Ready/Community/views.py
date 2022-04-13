import json
import time
from django.db.models import Q

from models.models import Community,CommunityTopic,TopicPost,PostImage
from . serializers import CommunitySerializer,TopicSerializers,PostSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid
from tools import common as utils

class CommAction(ModelViewSet):
    #增删改
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    lookup_field = "CommunityID"

    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, CommunityID):
        Comm=Community.objects.get(CommunityID=CommunityID)
        ser = CommunitySerializer(instance=Comm, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class TopicAction(ModelViewSet):
    queryset = CommunityTopic.objects.all()
    serializer_class = TopicSerializers
    lookup_field = "TopicID"


    @action(methods=['post'],detail=False,url_path="Create")
    def Create(self,request):
        CommunityID=request.data.get('CommunityID')
        check=Community.objects.filter(CommunityID=CommunityID)
        if not check:
            return Response({"result":"社区ID错误"},status=status.HTTP_400_BAD_REQUEST)

        Creator=request.user['UID']
        Time=int(time.time())
        HasImage=request.data.get('HasImage')
        Title=request.data.get('Title')
        if HasImage=="True":
            try:
                img=request.FILES.get('TopicPic')
                CommunityTopic.objects.create(CommunityID=CommunityID, Creator=Creator,
                                              Time=Time, HasImage=True, Title=Title, ImageUri=img)
            except Exception as e:
                print(e)
                return Response({"result":"save image faild"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"result": "ok"},status=status.HTTP_200_OK)

        else:
            try:
                CommunityTopic.objects.create(CommunityID=CommunityID,Creator=Creator,
                                              Time=Time,HasImage=False,Title=Title)
            except Exception as e:
                print(e)
                return Response({"result": "internal error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"result":"ok"},status=status.HTTP_200_OK)


    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, TopicID):
        topic = CommunityTopic.objects.get(TopicID=TopicID)
        ser = TopicSerializers(instance=topic, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

class ShowAllTopic(APIView):

    def get(self, request):
        CommID = request.data.get("CommunityID")
        topics = CommunityTopic.objects.filter(CommunityID=CommID)
        ser=TopicSerializers(instance=topics,many=True)
        return Response(ser.data)

class PostAction(ModelViewSet):
    queryset = TopicPost.objects.all()
    serializer_class = PostSerializers
    lookup_field = "PostID"

    @action(methods=['post'], detail=False, url_path="Create")
    def Create(self, request):

        TopicID = request.data.get('TopicID')
        check = CommunityTopic.objects.filter(TopicID=TopicID)
        if not check:
            return Response({"result": "主题ID错误"},status=status.HTTP_400_BAD_REQUEST)

        UID = request.user['UID']
        Time = int(time.time())
        HasImage = request.data.get('HasImage')
        Content = request.data.get('Content')
        if HasImage == "True":
            try:
                imgs = request.FILES.getlist('PostPic')
                t=TopicPost.objects.create(TopicID=TopicID, UID=UID,
                                              Time=Time, HasImage=True, Content=Content)
                for f in imgs:
                    PostImage.objects.create(PostID=t.PostID,Uri=f)

            except Exception as e:
                print(e)
                return Response({"result": "save image faild"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"result": "ok"},status=status.HTTP_200_OK)

        else:
            try:
                TopicPost.objects.create(TopicID=TopicID, UID=UID,
                                              Time=Time, HasImage=False, Content=Content)
            except Exception as e:
                print(e)
                return Response({"result": "internal error"})

            return Response({"result": "ok"},status=status.HTTP_200_OK)

class ShowAllPost(APIView):

    def get(self, request):
        TopicID = request.data.get("TopicID")
        posts = TopicPost.objects.filter(TopicID=TopicID)

        content={}
        itemList=[]
        for p in posts:
            if p.HasImage:
                picList=[]
                try:
                    imgs=PostImage.objects.filter(PostID=p.PostID)
                    for i in imgs:
                        picList.append(utils.HOST_PREFIX+i.Uri.url)
                except Exception as e:
                    print(e)
                    return Response({"result": "internal error"})
                item={}
                item['PostID']=p.PostID
                item['TopicID']=p.TopicID
                item['UID']=p.UID
                item['Time']=p.Time
                item['HasImage']=p.HasImage
                item['Content']=p.Content
                item['pics']=picList

                itemList.append(item)


            else:
                item = {}
                item['PostID'] = p.PostID
                item['TopicID'] = p.TopicID
                item['UID'] = p.UID
                item['Time'] = p.Time
                item['HasImage'] = p.HasImage
                item['Content'] = p.Content

                itemList.append(item)

        content['data']=itemList
        print(itemList)
        return Response(content, status=status.HTTP_200_OK)


