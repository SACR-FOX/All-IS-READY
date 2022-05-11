from django.urls import path
from . import views


urlpatterns = [

    path('Add/', views.Reward.as_view(), name="经验值外部逻辑接口"),
    path('Situation/',views.Situation.as_view(),name="个人学习数据查询"),
    path('Rank/',views.Rank.as_view(),name="学习排行榜")
    # path('AddAccumulation/',views.addAccumulation.as_view(),name="学习时长外部逻辑接口")


]
