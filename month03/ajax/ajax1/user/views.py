import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
# Create your views here.
def xhr(request):
    return render(request,'xhr.html')


def get_xhr(request):
    return render(request,'get-xhr.html')


def get_xhr_server(request):
    name = request.GET.get("uname")
    return HttpResponse('欢迎%s'%name)



def check_user(name):
    count_user = models.User.objects.filter(name = name)
    if len(count_user) == 0:
        return True
    else:
        return False


def xhr_regist(request):
    name = request.GET.get('uname')
    if check_user(name):
        return HttpResponse('0')
    else:
        return HttpResponse('1')


def regist(request):
    if request.method == "GET":
        return render(request,'regist.html')


def login(request):
    if request.method =="GET":
        return render(request,'login.html')
    elif request.method =="POST":
        print("OK")
        return HttpResponse("OK")
    else:
        return None


def regist_post(request):
    if request.method == "POST":
        uname = request.POST.get("uname","")
        upwd = request.POST.get("upwd","")
        if check_user(uname):
            auser = models.User.objects.create(name=uname,password = upwd)
            return HttpResponse("注册成功")
    return HttpResponse("注册失败")


def index(request):
    return render(request,'index.html')


def show(request):
    result = models.User.objects.all()
    res = ""
    for user in result:
        res = res+"|"+user.name+"_"+user.password
    return HttpResponse(res)

def json_dumps(request):
    # 方法一:
    # dic = {
    #     "uname":"lili",
    #     "age":"30"
    # }
    # jsom_str = json.dumps(dic)
    # return HttpResponse(jsom_str)

    # 方法二:
    dic1 = [{
        "uname": "lili",
        "age": 30
    },{
        "uname": "panghu",
        "age": 29
    },{
        "uname": "xiaofu",
        "age": 31
    },
    ]

    str2_json = json.dumps(dic1,sort_keys=True,separators=(",",":"))

    return HttpResponse(str2_json,content_type="application/json")

    # 方法三:
    # from django.core import serializers
    # user = models.User.objects.all()
    # user_all = serializers.serialize('json',user)
    # return HttpResponse(user_all,content_type="application/json")

    # 方法四:
    # users = models.User.objects.all()
    # l = []
    # for user in users:
    #     data = {}
    #     data["name"] = user.name
    #     data["password"] = user.password
    #     l.append(data)
    #
    # json_l = json.dumps(l)
    #
    #
    # return HttpResponse(json_l,content_type="application/json")