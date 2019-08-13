from django.http import HttpResponse


def page_view(reuqest):
    return HttpResponse(reuqest.GET.getlist())


def page1_view(reuqest):
    html = reuqest
    # html += "<h1>这是第一个Web页面</h1>"
    return HttpResponse(html)


def page2_view(reuqest):
    html = "<h1>这是第二个Web页面</h1>"
    return HttpResponse(html)


def pagen_view(request, n):
    html = "<h1>这是第%s个Web页面</h1>" % n
    return HttpResponse(html)


def get_num(request, n1, s1, n2):
    result = 0
    if s1 == "add":
        result = int(n1) + int(n2)
    elif s1 == "sub":
        result = int(n1) - int(n2)
    elif s1 == "mul":
        result = int(n1) * int(n2)

    html = "<h1>%s</h1>" % result
    return HttpResponse(html)


def gettel(request, **kwargs):
    html = "<h1>name:%s</h1>" % kwargs["name"]
    html += "<h1>tel:%s</h1>" % kwargs["tel"]
    return HttpResponse(html)


def get_bir(request, **kwargs):
    result = "%s年%s月%s日" % (kwargs["y"], kwargs["m"], kwargs["d"])

    return HttpResponse(result)


def mypage(request):
    if request.method == "GET":
        html = "a="+"/".join(request.GET.getlist("a"))

        return HttpResponse(html)
    else:
        return HttpResponse("不是get请求")
