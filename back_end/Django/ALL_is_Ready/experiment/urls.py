from django.urls import path
from . import views



urlpatterns = [

    path('oss', views.OSStest.as_view(), name="oss上传"),
    path('ranklist',views.requestTest.as_view(),name="rank"),
    path('modify_params',views.modify_params.as_view())

]