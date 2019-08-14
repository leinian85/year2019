from django.shortcuts import render


def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        base = request.POST.get("base",None)
        if base is None or base == "":
            return render(request, "index.html")

        base = float(base)
        is_city = request.POST.get("is_city")
        yl_g = base * 8 / 100
        yl_dw = base * 19 / 100
        sy_g = base * 0.2 / 100 if is_city == "1" else 0
        sy_dw = base * 0.8 / 100
        gs_g = 0
        gs_dw = base * 0.5 / 100
        sybx_g = 0
        sybx_dw = base * 0.8 / 100
        jbyl_g = base * 2 / 100 + 3
        jbyl_dw = base * 10 / 100
        gjj_g = base * 12 / 100
        gjj_dw = base * 12 / 100
        sum_g = yl_g + sy_g + gs_g + sybx_g + jbyl_g + gjj_g
        sum_dw = yl_dw + sy_dw + gs_dw + sybx_dw + jbyl_dw + gjj_dw
        sum = sum_g + sum_dw
        return render(request, "index.html",locals())
