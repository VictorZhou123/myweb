from django.contrib import admin
from .models import Blog
# Register your models here.
admin.site.register(Blog)       #将Blog类的模型注册到后台管理页面也就是admin页面