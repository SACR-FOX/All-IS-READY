from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
# router.register('Action',views.OrgAction,basename="OrgAction")
# router.register('Task/Action',views.OrgTaskAction,basename="OrgTaskAction")
urlpatterns = [
    #
    # path('Task/List',views.OrgTaskAll.as_view(),name="所有任务"),
    # path('Task/ACK',views.ACK.as_view(),name="查询接收状态"),
    # path('GroupImport',views.GroupImport.as_view(),name="批量导入"),
    # path('Statistics',views.ItemStatistics.as_view(),name="统计")

]+router.urls