from django.db import models


# Create your models here.

# 题目
class Question(models.Model):
    # varchar 数据类型
    # max_length 字段的长度
    # question varchar(200) 等同于如下语句
    question_text = models.CharField(max_length=200)
    # datetime 数据类型
    # pub_date datetime   等同于如下语句
    pub_date = models.DateTimeField()


# 选项
class Choice(models.Model):
    # to    外建关联表
    # on_delete 当删除主键数据的时候，是否联动删除外键的数据
    question = models.ForeignKey(to=Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # 整型，默认值为0


# 用户信息表
# 生成表名为  应用名_类名
class User(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    registerDate = models.DateTimeField()
    loginIp = models.CharField(max_length=15)

    # 自定义表名
    class Meta:
        db_table = 'UserInfo'

# 一个作者对应多本书，一本书只有一个作者 外键（一对多）
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person)

# 新建一个用户投票记录表
class vote_records(models.Model):
    user = models.ForeignKey(Person)
    question = models.ForeignKey(Question)
    time = models.DateTimeField()
# 一个作者对应多本书，一本书对应多个作者 外建（多对多）
class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)



