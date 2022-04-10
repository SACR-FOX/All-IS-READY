from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Detail',views.UserDetail,basename="UserDetail")
# router.register('Login',views.UserLogin,basename="UserLogin")




urlpatterns = [

    path('Login',views.UserLogin.as_view(),name="用户登录"),

]+router.urls
