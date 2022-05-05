from django.urls import path
from . import views


urlpatterns = [

    path('Add/', views.Reward.as_view(), name="经验值外部逻辑接口"),
    # path('AddAccumulation/',views.addAccumulation.as_view(),name="学习时长外部逻辑接口")


]
