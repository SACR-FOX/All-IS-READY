from django.urls import path
from . import views



urlpatterns = [

    path('oss',views.test.as_view(),name="oss上传"),

]