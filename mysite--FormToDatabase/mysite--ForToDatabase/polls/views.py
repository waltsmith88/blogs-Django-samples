from django.shortcuts import render
# render返回一个界面

# Create your views here.
from django.http import HttpResponse

# HttpResponse返回html形式解析文本


# def index(request):
#     # return HttpResponse('Hello world')
#     content = {}
#     content['title'] = "文章标题"
#     content['text'] = "你说的丰富历史的减肥是来得及发垃圾搜发我二十多岁设计费老师的京东方啥都没说砥砺奋进沃尔沃累了就舒服了"
#     return render(request, 'index.html', content)

# views.py代码
# def index1(request):
#     from polls.models import Person
#     person = Person.objects.all()
#     content = {}
#     content['person'] = person
#     # return render(request, 'index.html', content)

# views.py代码
def index(request):
    content = {}
    i = [i for i in range(10)]
    content['i'] = i
    return render(request, 'index.html', content)

# 两个数相加，采用add/a/b形式访问
def add_two(request, a, b):
    return HttpResponse(str(int(a)+int(b)))

# 两个数相加，采用add/?a=value&b=value形式访问
def add_a_b(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(str(int(a)+int(b)))

# 操作数据库，增加用一个用户数据
def addPerson(request, name, age):
    # 导入Person类
    from polls.models import Person
    # 实例化一个Person对象p
    p = Person()
    # 设p对象的属性
    p.name = name
    p.age = age
    # 保存数据p
    p.save()
    return HttpResponse('保存成功%d' % p.id)


# 查找数据库表Person中的单条数据，返回
def getPerson(request, id):
    # 导入Person类
    from polls.models import Person
    # 实例化一个Person对象p
    p = Person.objects.get(id=int(id))
    # p = Person.objects.raw('select * from polls_person where id=%d' % id)
    return HttpResponse('查询成功%d\n姓名：%s\n年龄：%s' % (p.id, p.name, p.age))

# 取文章
def getword(request, id):
    from polls.models import Person
    # 实例化一个对象
    # p = Person.objects.get(id=int(id))
    # p = Person.objects.all()[int(id)-1]
    p = Person.objects.all()[10*(int(id)-1):10*int(id)]
    return HttpResponse(list(p))
    # return HttpResponse("正文：%s" % p.name)


# def getword(request, id1, id2):
#     from polls.models import Person
#     p = Person.objects.filter()


# views.py代码
def getbooks(request):
    from polls.models import Book
    book = Book.objects.all()
    content = {}
    content['book'] = book
    i = [i for i in range(10)]
    content['i'] = i
    return render(request, 'books.html', content)

# url()方法返回一个拼接地址
# def urltest(request, a, b):
#     content={}
#     content['url'] =

# views.py代码
def customFilter(request, html_str):
    content = {}
    content['html_str'] = html_str
    return render(request, 'customFilter.html', content)

##==================== 20171221 20:21
# 作业：建立一个图书列表页面，显示图书名列表，
# 并实现点击书名跳转到图书详细页面，显示图书详细信息
def booklist(request):
    # 导入图书类
    from polls.models import Book
    # 实例化一个图书对象
    books = Book.objects.all()
    # 建立空字典存储booklist
    dict_book = {}
    dict_book['booklist'] = books
    # 向Html页面传入数据booklist
    return render(request, 'bookList.html', dict_book)

# 获取书籍信息
def bookinfo(request, id):
    # 导入图书类
    from polls.models import Book
    # 实例化一个图书对象
    book = Book.objects.get(id=id)
    # 建立空字典存储booklist
    dict_book = {}
    dict_book['book'] = book.name
    dict_book['author'] = book.person.name
    dict_book['author_age'] = book.person.age
    return render(request, 'bookInfo.html', dict_book)



##======================== 20171222 10:50
## 内置过滤器测试
def filter_test(request, value):
    # 参数value
    # value = 'a \n b \n c'
    return render(request, 'filterTest.html', {'value': value})


# ## 内置过滤器linenumbers测试专用
# def filter_test(request, value):
#     # 参数value
#     value = 'a \n b \n c'
#     return render(request, 'filterTest.html', {'value': value})


# ## 内置过滤器dictsort与dictsortreversed测试专用
# def filter_Test(request, arg):
#     # 参数arg
#     arg = [
#     {'name': 'zed', 'age': 19},
#     {'name': 'amy', 'age': 22},
#     {'name': 'joe', 'age': 31},
# ]
#     return render(request, 'filterTest.html', {'arg': arg})


## 内置过滤器date测试专用
# def filter_Test(request, arg):
#     # 参数arg
#     from datetime import datetime
#     arg = datetime.now()
#     return render(request, 'filterTest.html', {'arg': arg})


##======================== 20171222 10:50
## 利用表单增加图书，实现前台与数据库交互
def addbook(request):
    return render(request, 'bookadd.html')

# 向图书馆增加数据GET方法
def addbooktodatabase(request):
    # 获取参数book_name,author,author_age
    if request.method == "GET":
        book_name = request.GET["book_name"]
        author_name = request.GET["author"]
        author_age = request.GET["author_age"]
    else:
        book_name = request.POST["book_name"]
        author_name = request.POST["author"]
        author_age = request.POST["author_age"]

    ## 先增加作者信息
    from polls.models import Person
    person = Person()
    person.name = author_name
    person.age = author_age
    person.save()
    ## 增加图书信息
    from polls.models import Book
    bookadded = Book(name=book_name)
    # bookadded = Book()
    # bookadded.name = bookname
    # 保存修改
    bookadded.person_id = person.id
    bookadded.save()
    # 重定向
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/addok/')

# 返回页面addok
def addok(request):
    return render(request, 'addok.html')

