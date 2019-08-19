from django.contrib import admin
from . import models
# Register your models here.


class AuthorManage(admin.ModelAdmin):
    list_display = ["name"]

class BookManage(admin.ModelAdmin):
    list_display = ["title"]

admin.site.register(models.Author,AuthorManage)
admin.site.register(models.book,BookManage)