from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30,
                             null=False,
                             unique=True,
                             verbose_name="书名")
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                default=0.0,
                                verbose_name="定价")
    pub = models.CharField(max_length=100,
                           null=False,
                           default="",
                           verbose_name="出版社")
    market_price = models.DecimalField(decimal_places=2,
                                       max_digits=7,
                                       default=0.0,
                                       verbose_name="市场价")

    class Meta:
        db_table = "book"
        verbose_name = '书籍'
        verbose_name_plural = '书籍表'

class Author(models.Model):
    name = models.CharField(max_length=40,
                            null=False,
                            verbose_name="姓名")
    age = models.IntegerField(null=False,
                              default=1,
                              verbose_name="年龄")
    email = models.EmailField(max_length=100,
                              null=True,
                              verbose_name="邮箱")

    class Meta:
        db_table = "author"
        verbose_name = '作者'
        verbose_name_plural = '作者表'
