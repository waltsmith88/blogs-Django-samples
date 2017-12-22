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



