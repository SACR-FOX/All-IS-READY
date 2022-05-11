from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('Detail',views.UserDetail,basename="UserDetail")
# router.register('Login',views.UserLogin,basename="UserLogin")




urlpatterns = [

    path('Login',views.UserLogin.as_view(),name="用户登录"),
    # path('Rank',views.Rank.as_view(),name="经验值排名"),
    path('Register',views.UserRegister.as_view(),name="用户注册"),

]+router.urls
