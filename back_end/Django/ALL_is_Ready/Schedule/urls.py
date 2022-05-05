from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Action',views.ScheduleAction,basename="ScheduleAction")
router.register('',views.Schedule_today,basename="Today")
router.register('',views.Schedule_next,basename="Next")
urlpatterns = [

    path('GroupImport',views.GroupImport.as_view(),name="批量导入"),


]+router.urls
