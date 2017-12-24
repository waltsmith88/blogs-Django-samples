from django.shortcuts import render
# render返回一个界面

# Create your views here.
from django.http import HttpResponse


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


