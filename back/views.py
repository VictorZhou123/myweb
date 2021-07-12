from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Blog,User
from django.urls import reverse
from .form import UserForm

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request,'back/index.html',{'blogs':blogs})

def add(request):
    if request.method == 'GET':
        return render(request,'back/add.html',)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog.objects.create(title=title,content=content)
        # return redirect('/back/') #新增成功，重定向到主页
        return redirect(reverse('back:index'))  #用revers生成路由地址


def delete(request,bid):
    blog = Blog.objects.get(pk=bid)
    if blog:
        blog.delete()
        return redirect(reverse('back:index')) #用revers生成路由地址


def edit(request,bid):
    if request.method == 'GET':
        blog = Blog.objects.get(pk=bid)
        return render(request,'back/edit.html',{'blog':blog})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog = Blog.objects.get(pk=bid)
        blog.title = title
        blog.content = content
        blog.save()
        # return redirect('/back/') #新增成功，重定向到主页
        return redirect(reverse('back:index'))  #用revers生成路由地址

def detail(request,bid):
    blog = Blog.objects.get(pk=bid)
    # title = blog.title
    # content = blog.content
    return render(request,'back/detail.html',{'blog':blog})

def reg(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request,'back/auth/reg.html',{'form':form})
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            # username = user.cleaned_data.get('username')
            # password = user.cleaned_data.get('password')
            # User.objects.create(username=username,password=password)
            User.objects.create(** user.cleaned_data)   #传位置参数，cleaned_data是一个字典的结果
            return redirect('back:login')
        return render(request,'back/auth/reg.html',{'form':user})

def login(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request,'back/auth/login.html',{'form':form})
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            users = User.objects.filter(**user.cleaned_data)
            if users:
                request.session['user'] = users[0].username
                return redirect(reverse('back:index'))
        return render(request,'back/auth/login.html',{'form':user})

def logout(request):
    request.session.flush()
    return redirect(reverse('back:login'))