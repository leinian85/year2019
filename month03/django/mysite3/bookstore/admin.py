from django.contrib import admin
from . import models
# Register your models here.

class BookManage(admin.ModelAdmin):
    list_display = ["id","title","price","market_price","pub"]
    list_filter = ["pub"]
    list_display_links = ["title"]
    search_fields = ["title","price"]
    list_editable = ["market_price"]


class AuthorManage(admin.ModelAdmin):
    list_display = ["id","name","age","email"]
    search_fields = ["name"]
    list_display_links = ["name"]

admin.site.register(models.Book,BookManage)
admin.site.register(models.Author,AuthorManage)
