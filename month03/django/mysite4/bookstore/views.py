from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set_cookies_view(request):
    resp = HttpResponse("OK")
    resp.set_cookie("myvar",100)
    return resp