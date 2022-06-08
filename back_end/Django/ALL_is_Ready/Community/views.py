import json
import time
from django.db.models import Q

import tools.common
from models.models import Community,CommunityTopic,TopicPost,PostImage,User,CommunityStars
from . serializers import CommunitySerializer,TopicSerializers,PostSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from . import pagination
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid
from tools import common as utils
from tools import common as CommonTools
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


class CommAction(ModelViewSet):
    #增删改
    queryset = Community.objects.all().order_by("-PostCount","-Renewal")
    serializer_class = CommunitySerializer
    lookup_field = "CommunityID"
    pagination_class = pagination.CommunityNumberPagination

    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, CommunityID):
        try:
            Comm=Community.objects.get(CommunityID=CommunityID)
        except Exception:
            return Response({"result":"CommunityID not match"},status=status.HTTP_404_NOT_FOUND)

        if request.user['UID']!=Comm.AdministratorID:
            return Response({"result": "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)

        newDict = {}
        if request.data.get('CommunityName'):
            newDict['CommunityName'] = request.data.get('CommunityName')
        if request.data.get('CommunityName'):
            newDict['Description'] = request.data.get('Description')
        if request.data.get('AdministratorID'):
            newID =int(request.data.get('AdministratorID'))
            try:
                User.objects.get(UID=newID)
            except Exception:
                return Response({"result":"user not exit"},status=status.HTTP_404_NOT_FOUND)
            newDict['AdministratorID']=newID


        try:
            img = request.FILES.get('Poster')
        except Exception :
            return Response({"result": "get pic failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if img:
            Comm.Poster.delete()
            newDict['Poster'] = img


        ser = CommunitySerializer(instance=Comm, data=newDict, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class TopicAction(ModelViewSet):
    queryset = CommunityTopic.objects.all().order_by('-Stars','-Time')
    serializer_class = TopicSerializers
    lookup_field = "TopicID"


    @action(methods=['post'],detail=False,url_path="Create")
    def Create(self,request):
        CommunityID=request.data.get('CommunityID')
        check=Community.objects.filter(CommunityID=CommunityID)
        if not check:
            return Response({"result":"社区ID错误"},status=status.HTTP_400_BAD_REQUEST)

        Comm = Community.objects.get(CommunityID=CommunityID)

        UID=request.user['UID']
        Time=int(time.time())
        HasImage=request.data.get('HasImage')
        Title=request.data.get('Title')
        if HasImage=="True":
            try:
                img=request.FILES.get('TopicPic')
                print(img)
                CommunityTopic.objects.create(CommunityID=CommunityID, UID=UID,
                                              Time=Time, HasImage=True, Title=Title, ImageUri=img,Stars=0)
            except Exception as e:
                print(e)
                return Response({"result":"save image faild"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        else:
            try:
                CommunityTopic.objects.create(CommunityID=CommunityID,Creator=UID,
                                              Time=Time,HasImage=False,Title=Title,Stars=0)
            except Exception as e:
                print(e)
                return Response({"result": "internal error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # EXP
        usr = User.objects.get(UID=UID)
        CommonTools.addEXP(usr, 5)
        # CommonTools.EXP2Rank(usr.EXP)

        # update community renewal
        Comm.Renewal=Time
        Comm.PostCount+=1
        Comm.save()

        return Response({"result": "ok"}, status=status.HTTP_200_OK)


    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, TopicID):

        try:
            topic = CommunityTopic.objects.get(TopicID=TopicID)

        except Exception as e:
            print(e)
            return Response({"result":"ID not Match"},status=status.HTTP_404_NOT_FOUND)

        if request.user['UID'] != topic.UID:
            return Response({"result": "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)

        newDict={}
        if request.data.get('Title'):
            newDict['Title'] = request.data.get('Title')
        if request.data.get('HasImage')=='False':
            newDict['HasImage']=True
        elif request.data.get('HasImage')=='True':
            try:
                img = request.FILES.get('TopicPic')

            except Exception as e:
                print(e)
                return Response({"result":"get pic failed"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            if img:
                topic.ImageUri.delete()
                newDict['HasImage']=True
                newDict['ImageUri']=img
            else:
                topic.ImageUri.delete()
                newDict['HasImage'] = False
                newDict['ImageUri'] = CommonTools.HOST_PREFIX+CommonTools.DEFAULT_PIC

        ser = TopicSerializers(instance=topic, data=newDict, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    @action(methods=['post'],detail=True,url_path="Star")
    def Star(self,request,TopicID):
        try:
            topic = CommunityTopic.objects.get(TopicID=TopicID)
        except Exception :
            return Response({"result": "TopicID don't match"}, status=status.HTTP_404_NOT_FOUND)


        #if repeat
        check=CommunityStars.objects.filter(Q(UID=request.user['UID']),Q(TargetID=topic.TopicID),Q(type=0))

        if not check:
            #add star record
            try:
                CommunityStars.objects.create(TargetID=topic.TopicID,UID=request.user['UID'],type=0)
                topic.Stars+=1
                topic.save()

            # add EXP
                auth=User.objects.get(UID=topic.UID)
                CommonTools.addEXP(auth,10)

            except Exception as e:
                print(e)
                return Response({'result':'internal err'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'result': 'ok'}, status=status.HTTP_200_OK)

        else:
            return Response({'result':'already thumbed'},status=status.HTTP_403_FORBIDDEN)

class ShowAllTopic(APIView):

    def get(self,request):
        CommID =request.query_params.get("CommunityID")
        Page=request.query_params.get("page")
        if not Page:
            Page = 1
        else:
            Page = int(Page)
        All=CommunityTopic.objects.filter(CommunityID=CommID).order_by('-Stars','-Time')
        paginator = Paginator(All, 12)
        try:
            page=paginator.page(Page)
        except Exception:
            return Response({"result":"empty"},status=status.HTTP_200_OK)
        content={}
        if page.has_next():
            content['next'] = True
        else:
            content['next'] = False
        if page.has_previous():
            content['previous'] = True
        else:
            content['previous'] = False
        content['count'] = paginator.count
        itemlist=[]
        for p in page.object_list:
            usr=User.objects.filter(UID__exact=p.UID).first()
            item={}
            item['TopicID']=p.TopicID
            item['UID']=usr.UID
            item['header']=tools.common.HOST_PREFIX+usr.Header.url
            item['Creator']=usr.Uname
            item['Time']=p.Time
            item['HasImage']=p.HasImage
            if p.HasImage:
                item['ImageUri']=tools.common.HOST_PREFIX+p.ImageUri.url
            item['Title']=p.Title
            item['Stars']=p.Stars
            itemlist.append(item)
        content['data']=itemlist
        return Response(content,status=status.HTTP_200_OK)




class PostAction(ModelViewSet):
    queryset = TopicPost.objects.all()
    serializer_class = PostSerializers
    lookup_field = "PostID"

    @action(methods=['post'], detail=False, url_path="Create")
    def Create(self, request):

        TopicID = request.data.get('TopicID')
        check = CommunityTopic.objects.filter(TopicID=TopicID)
        if not check:
            return Response({"result": "话题ID错误"},status=status.HTTP_400_BAD_REQUEST)

        UID = request.user['UID']
        Time = int(time.time())
        HasImage = request.data.get('HasImage')
        Content = request.data.get('Content')
        if HasImage == "True":
            try:
                imgs = request.FILES.getlist('PostPic')
                print(imgs)
                t=TopicPost.objects.create(TopicID=TopicID, UID=UID,
                                              Time=Time, HasImage=True, Content=Content)
                for f in imgs:
                    PostImage.objects.create(PostID=t.PostID,Uri=f)

            except Exception as e:
                print(e)
                return Response({"result": "save image faild"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        else:
            try:
                TopicPost.objects.create(TopicID=TopicID, UID=UID,
                                              Time=Time, HasImage=False, Content=Content)
            except Exception as e:
                print(e)
                return Response({"result": "internal error"})

        # EXP
        usr = User.objects.get(UID=UID)
        CommonTools.addEXP(usr, 5)
        # CommonTools.EXP2Rank(usr.EXP)

        return Response({"result": "ok"},status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="Star")
    def Star(self, request, PostID):
        try:
            post=TopicPost.objects.get(PostID=PostID)
        except Exception:
            return Response({"result":"PostID don't match"}, status=status.HTTP_404_NOT_FOUND)

        # if repeat
        check = CommunityStars.objects.filter(Q(UID=request.user['UID']), Q(TargetID=post.PostID), Q(type=1))

        if not check:
            # add star record
            try:
                CommunityStars.objects.create(TargetID=post.PostID, UID=request.user['UID'], type=1)
                post.Stars+=1
                post.save()

                # add EXP
                auth = User.objects.get(UID=post.UID)
                CommonTools.addEXP(auth, 10)

            except Exception as e:
                print(e)
                return Response({'result': 'internal err'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'result': 'ok'}, status=status.HTTP_200_OK)

        else:
            return Response({'result': 'already thumbed'}, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['put'], detail=True, url_path="Modify")
    def Modify(self, request, PostID):

        try:
            posts=TopicPost.objects.get(PostID=PostID)
        except Exception as e:
            print(e)
            return Response({"result": "ID not Match"},status=status.HTTP_404_NOT_FOUND)


        if request.data.get('HasImage')=='False':
            newDict={}
            newDict['HasImage']=True
            if request.data.get('Content'):
                newDict['Content']=request.data.get('Content')

            ser = PostSerializers(instance=posts, data=newDict, partial=True)
            ser.is_valid(raise_exception=True)
            ser.save()
            return Response(ser.data)

        elif request.data.get('HasImage')=='True':
            pics=PostImage.objects.filter(PostID=PostID)
            pics.delete()

            newDict = {}
            newDict['HasImage'] = True
            if request.data.get('Content'):
                newDict['Content'] = request.data.get('Content')

            try:
                imgs = request.FILES.getlist('PostPic')
                if  imgs:
                    for f in imgs:
                        PostImage.objects.create(PostID=PostID,Uri=f)
                else:
                    newDict['HasImage']=False

            except Exception as e:
                print(e)
                return Response({"result": "save image faild"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            ser = PostSerializers(instance=posts, data=newDict, partial=True)
            ser.is_valid(raise_exception=True)
            ser.save()
            return Response(ser.data)

class ShowAllPost(APIView):

    def get(self, request):
        TopicID = request.query_params.get("TopicID")
        page=request.query_params.get("page")
        if not page:
            page = 1
        else:
            page=int(page)

        posts = TopicPost.objects.filter(TopicID=TopicID).order_by('-Time','-Stars')
        paginator=Paginator(posts,12)
        Page=paginator.page(page)

        content={}
        if Page.has_next():
            content['next']=True
        else:
            content['next'] = False
        if Page.has_previous():
            content['previous'] = True
        else:
            content['previous'] = False
        content['count']=paginator.count

        itemList=[]
        for p in Page.object_list:
            usr = User.objects.filter(UID__exact=p.UID).first()
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
                item['header']=tools.common.HOST_PREFIX+usr.Header.url
                item['Creator']=usr.Uname
                item['Time']=p.Time
                item['HasImage']=p.HasImage
                item['Content']=p.Content
                item['pics']=picList
                item['Stars']=p.Stars

                itemList.append(item)


            else:
                item = {}
                item['PostID'] = p.PostID
                item['TopicID'] = p.TopicID
                item['UID'] = p.UID
                item['header'] = tools.common.HOST_PREFIX+usr.Header.url
                item['Creator'] = usr.Uname
                item['Time'] = p.Time
                item['HasImage'] = p.HasImage
                item['Content'] = p.Content
                item['Stars'] = p.Stars

                itemList.append(item)

        content['result']=itemList
        return Response(content, status=status.HTTP_200_OK)

class CheckStarCondition(APIView):
    def post(self,requset):
        ID=requset.data.get('ID')
        type=requset.data.get('type')
        UID=requset.user['UID']

        try:
            check=CommunityStars.objects.get(TargetID=ID,type=type,UID=UID)
            if check:
                return Response({"result": True}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"result":False},status=status.HTTP_200_OK)


