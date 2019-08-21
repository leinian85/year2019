from django.shortcuts import render
from . import forms
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request,"regist/index.html")
    elif request.method == "POST":
        form1 = forms.LoginForm(request.POST)
        if form1.is_valid():
            return HttpResponse('OK')
        else:
            error = dict(form1.errors)
            if "__all__" in form1.errors:
                other_error = form1.errors["__all__"][0]
            return render(request,"regist/index.html",locals())
