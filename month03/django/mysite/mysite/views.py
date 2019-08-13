from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def list(request):
    return render(request, "list.html")

def mypic(request):
    return render(request, "mypic.html")

def login(request):
    return render(request, "login.html")
