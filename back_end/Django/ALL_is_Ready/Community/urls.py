from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Action',views.CommAction,basename="CommAction")
router.register('Topic', views.TopicAction, basename="CommTopic")
router.register('Post',views.PostAction,basename="TopicPost")
urlpatterns = [
    #
    path('Topic/All',views.ShowAllTopic.as_view(),name="所有话题"),
    path('Post/All',views.ShowAllPost.as_view(),name="所有帖子"),
    # path('GroupImport',views.GroupImport.as_view(),name="批量导入"),
    # path('Statistics',views.ItemStatistics.as_view(),name="统计")

]+router.urls