from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Action',views.ScheduleAction,basename="ScheduleAction")
urlpatterns = [
    path('GroupImport/',views.GroupImport.as_view(),name="批量导入"),
    path('byDay/', views.Schedule_byday.as_view(), name="今日课表"),
    path('Next/',views.Schedule_next.as_view(),name="下节课程信息"),
]+router.urls
