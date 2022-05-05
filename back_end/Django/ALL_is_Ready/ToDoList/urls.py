from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Action',views.ListAction,basename="ListAction")

urlpatterns = [

    path('All',views.ListAll.as_view(),name="所有计划"),
    path('Today',views.ListToday.as_view(),name="今日计划"),
    path('GroupImport',views.GroupImport.as_view(),name="批量导入"),
    path('Statistics',views.ItemStatistics.as_view(),name="统计")

]+router.urls
