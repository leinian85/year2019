from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def xhr(request):
    return render(request,'xhr.html')


def get_xhr(request):
    return render(request,'get-xhr.html')


def get_xhr_server(request):
    name = request.GET.get("uname")
    return HttpResponse('欢迎%s'%name)




def xhr_regist(request):
    name = request.GET.get('uname')
    try:
        user = models.User.objects.get(name = name)
        print(name, "  1")
        return HttpResponse('用户名已经存在!')
    except:
        print(name, "  2")
        return HttpResponse('OK')


def regist(request):
    return render(request,'regist.html')


def login(request):
    if request.method =="GET":
        return render(request,'login.html')
    elif request.method =="POST":
        print("OK")
        return HttpResponse("OK")
    else:
        return None