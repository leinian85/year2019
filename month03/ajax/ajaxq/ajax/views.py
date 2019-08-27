import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def load(request):
    return render(request,"load.html")


def load_server(request):
    return render(request,"load_server.html")

def jquery_get(request):
    return render(request,'jquery_get.html')

def jquery_get_server(request):
    name_list = []
    d = {"name":"王大锤","age":28}
    name_list.append(d)
    name=request.GET.get("name")
    age=request.GET.get("age")
    name_list.append({"name":name,"age":age})
    return HttpResponse(json.dumps(name_list),content_type='application/json')


def jquery_post_server(request):
    d = {"msg":"this psot is OK","code":10000}
    return HttpResponse(json.dumps(d),content_type='application/json')


def jquery_post(request):
    return render(request,'jquery_post.html')


def jquery_ajax(request):
    return render(request,'jquery_ajax.html')

def jquery_ajax_server(request):
    d = {"name":"铁锤公主","age":18}
    return HttpResponse(json.dumps(d),content_type='application/json')


def ajax_list(request):
    return render(request, 'ajax_list.html')

def ajax_list_server(request):
    d = [{"name":"王大锤","age":18},{"name":"铁锤妹妹","age":17}]
    return HttpResponse(json.dumps(d),content_type='application/json');


def cross(request):
    return render(request,'cross.html')

# def cross_server(request):
#     func = request.GET.get("callback")
#     d = {"name": "王大锤", "age": 18}
#     return HttpResponse(func+"("+json.dumps(d)+")")

def cross_server(request):
    return HttpResponse(func+"("+json.dumps(d)+")")