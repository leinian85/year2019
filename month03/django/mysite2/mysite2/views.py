from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

login_html = """
<form method="post" action="/login">
    姓名:<input type="text" name="name">
    密码:<input type="password" name="password">
    <input type="submit" value="提交">
</form>
"""


# http://127.0.0.1:8000/sum?start=整数&stop=整数&step整=字
def sum_view(request):
    if request.method == "GET":
        try:
            start = int(request.GET.get("start", 1))
            stop = int(request.GET.get("stop"))
            step = int(request.GET.get("step", 1))
            result = sum(range(start, stop, step))

            html = "<h1>sum:%s</h1>" % result

            return HttpResponse(html)
        except:
            html = "<h1>链接无效</h1>"
            return HttpResponse(html)


def login(request):
    if request.method == "GET":
        return HttpResponse(login_html)
    elif request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        # html = "姓名:%s 密码:%s"%(name,pwd)
        html = dict(request.POST).get("name")

        return HttpResponse(html)


# 方法一:
# def login2(request):
#     if request.method == "GET":
#         t = loader.get_template("mylogin.html")
#         html = t.render()
#         return HttpResponse(html)
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         pwd = request.POST.get("password")
#         dic = {"name":name,"pwd":pwd}
#
#         t = loader.get_template("result.html")
#         html = t.render(dic)
#         return HttpResponse(html)

# 方法二:
def login2(request):
    if request.method == "GET":
        t = loader.get_template("mylogin.html")
        html = t.render()
        return HttpResponse(html)
    elif request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        # dic = {"name":name,"pwd":pwd}
        list = [{"name": "张无忌", "pwd": 21}, {"name": "赵敏", "pwd": 22}]
        dic = {'list':list}
        return render(request, "result.html", dic)

def mycal(request):
    if request.method == "GET":
        return render(request,"mycal.html")
    elif request.method == "POST":
        x = int(request.POST.get("x"))
        y = int(request.POST.get("y"))
        flag = request.POST.get("sel")
        if flag == "add":
            cal = x + y
        elif flag == "sub":
            cal = x - y
        elif flag == "mul":
            cal = x * y
        elif flag == "div":
            cal = x / y
        return render(request,"mycal.html",locals())

def test_for(request):
    if request.method == "GET":
        lst = ["北京","上海","广州","深圳"]
        return render(request,"test_for.html",locals())

