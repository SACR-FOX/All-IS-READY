from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
# router.register('Detail',views.Detail,basename="FileDetail")
# router.register('Topic', views.TopicAction, basename="CommTopic")
# router.register('Post',views.PostAction,basename="TopicPost")
urlpatterns = [
    #
    path('upload', views.Upload.as_view(), name="文件上传"),
    path('FileList',views.FileList.as_view()),
    path('FolderList',views.FolderList.as_view()),
    path('OnlinePreview',views.OnlinePreview.as_view()),
    # path('Post/All',views.ShowAllPost.as_view(),name="所有帖子"),
    # path('GroupImport',views.GroupImport.as_view(),name="批量导入"),
    # path('Statistics',views.ItemStatistics.as_view(),name="统计")

]+router.urls