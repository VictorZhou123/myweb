from django.urls import path
from . import views

app_name = 'back'
urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('edit/<int:bid>',views.edit,name='edit'),
    path('detail/<int:bid>',views.detail,name='detail'),
    path('delete/<int:bid>',views.delete,name='delete'),

    path('auth/reg/',views.reg,name='reg'),
    path('auth/login/',views.login,name='login'),
    path('auth/logout/',views.logout,name='logout'),
]