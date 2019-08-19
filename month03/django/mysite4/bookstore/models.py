from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")

class book(models.Model):
    title = models.CharField(max_length=30,verbose_name="书名")
    author= models.ManyToManyField(Author,null=True)