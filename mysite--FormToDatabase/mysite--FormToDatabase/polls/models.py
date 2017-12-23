from django.db import models


# Create your models here.



# 一个作者对应多本书，一本书只有一个作者 外键（一对多）
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person)


# 一个作者对应多本书，一本书对应多个作者 外建（多对多）
class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)



