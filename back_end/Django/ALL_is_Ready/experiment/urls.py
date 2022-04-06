from django.urls import path
from . import views



urlpatterns = [

    path('sday',views.test.as_view(),name="批量导入"),

]