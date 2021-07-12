from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog

def index(request):
    blogs = Blog.objects.all()                                      #调用blog模块中的models文件的Blog类，输出其所有数据
    # titles = [blog.title for blog in blogs]
    # return HttpResponse(','.join(titles))                         #在front页面中显示两个title的联结
    return render(request,'front/list.html',{'blogs':blogs})        #blogs传入html文件内

def detail_path(request,bid):
    blog = Blog.objects.get(pk=bid)
    return render(request,'front/detail.html',{'blog':blog})

def detail_querystring(request):
    bid = request.GET.get('bid')                                    #GET属性输出类似于字典的数据
    blog = Blog.objects.get(pk = int(bid))
    return render(request, 'front/detail.html', {'blog': blog})