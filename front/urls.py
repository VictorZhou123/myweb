from django.urls import path
from . import views

app_name = 'front'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:bid>/',views.detail_path,name='detail_path'),  #设置路由，起名字'detail_path'，路径是"...detail/<int:bid>/"相当于deail_path代表了这个路径
    path('detail2/',views.detail_querystring,name='detail_querystring')
]