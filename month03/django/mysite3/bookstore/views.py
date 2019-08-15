from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request,"bookstore/index.html")

def insert(request):
    if request.method =="GET":
        return render(request,"bookstore/insert.html",)
    elif request.method =="POST":
        try:
            title = request.POST.get('title')
            price = request.POST.get('price')
            market_price = request.POST.get('market_price')
            pub = request.POST.get('pub')
            book = models.Book()
            book.title = title
            book.price = price
            book.market_price = market_price
            book.pub = pub
            book.save()
            msg = "添加成功!"
        except Exception as e:
            msg = e

        return render(request,"bookstore/insert.html",locals())

def add_author(request):
    if request.method == "GET":
        return render(request,"bookstore/add_author.html")
    elif request.method == "POST":
        try:
            name = request.POST.get('name')
            name = None if name == "" else name
            age = request.POST.get('age')
            email = request.POST.get('email')
            person = models.Author()
            person.name = name
            person.age = age
            person.email = email
            person.save()
            msg = "添加成功!"
        except Exception as e:
            msg = e

        return render(request,"bookstore/add_author.html",locals())

def show_book(request):
    name = request.POST.get("name")
    minprice = request.POST.get("minprice")
    maxprice = request.POST.get("maxprice")
    search_dic = {}
    if name:
        search_dic["title"] = name
    if minprice:
        search_dic["price__gt"] = minprice
    if maxprice:
        search_dic["price__lt"] = maxprice

    bookset = models.Book.objects.filter(**search_dic)
    return bookset

def show_author(request):
    name = request.POST.get("name")

    search_dic = {}
    if name:
        search_dic["name"] = name
    authorset = models.Author.objects.filter(**search_dic)

    return authorset

def serach(request):
    if request.method =="GET":
        return render(request,"bookstore/serach.html")
    elif request.method =="POST":
        s_type = request.POST.get("s_type")
        if s_type == "1":
            bookset = show_book(request)
        else:
            authorset = show_author(request)
        return render(request, "bookstore/serach.html",locals())

def book_delete(request):
    id = request.GET.get("id")
    try:
        book = models.Book.objects.filter(id = id)
        book.delete()
        msg = "删除成功!"
    except Exception as e:
        msg = e

    return render(request,"bookstore/serach.html",locals())

def update_book(request):
    if request.method == "GET":
        id = request.GET.get("id","0")
        book = models.Book.objects.get(id=id)
        return render(request,"bookstore/update_book.html",locals())
    if request.method == "POST":
        try:
            id = request.POST.get("id", "0")
            title = request.POST.get('title')
            price = request.POST.get('price')
            market_price = request.POST.get('market_price')
            pub = request.POST.get('pub')
            book = models.Book.objects.get(id = id)
            book.title = title
            book.price = price
            book.market_price = market_price
            book.pub = pub
            book.save()
            msg = "修改成功!"
        except Exception as e:
            msg = e

        return render(request,"bookstore/update_book.html",locals())

