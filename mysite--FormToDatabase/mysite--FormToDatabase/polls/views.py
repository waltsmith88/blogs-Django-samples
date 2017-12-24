from django.shortcuts import render
# render返回一个界面

# Create your views here.
from django.http import HttpResponse

# HttpResponse返回html形式解析文本

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
## 利用表单增加图书，实现前台与数据库交互
def addbook(request):
    return render(request, 'bookadd.html')

# 向图书馆增加数据GET或POST方法，且判断作者是否已经存在
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

    # 导入类Person
    from polls.models import Person
    ## 增加图书信息
    from polls.models import Book
    bookadded = Book(name=book_name)

    # 判断作者是否已存在
    person1 = Person.objects.filter(name=author_name)
    # 若作者已存在，则不添加作者
    if person1.exists() != 0:
        bookadded.person_id = person1[0].id
    else:
        # 作者不存在，增加作者信息
        person = Person()
        person.name = author_name
        person.age = author_age
        person.save()
        bookadded.person_id = person.id
    # 保存修改
    bookadded.save()
    # 重定向
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/addok/')


# 返回页面addok
def addok(request):
    return render(request, 'addok.html')

