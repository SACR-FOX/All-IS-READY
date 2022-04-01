from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Detail',views.UserDetail,basename="UserDetail")
router.register('Action',views.UserDetail,basename="UserAction")




urlpatterns = [

    # path('register/<UID>',views.UserAPI.as_view(),name="用户注册"),

]+router.urls
