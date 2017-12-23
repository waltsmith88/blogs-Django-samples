"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 导入路由，支持正则表达式
from django.conf.urls import url
from django.contrib import admin

# 导入控制器文件views.py
from polls import views as polls_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', polls_views.index),
    # url(r'^add/(\d+)/(\d+)/$', polls_views.add_two),
    url(r'^add/', polls_views.add_a_b),
    # 匹配addPerson/str/int/
    url(r'^addPerson/(\w+)/(\w+)/$', polls_views.addPerson),
    # 匹配getPerson/int/
    url(r'^getPerson/(\d+)/$', polls_views.getPerson),
    # 匹配word/int
    url(r'^word/(\d+)/$', polls_views.getword),

    url(r'^getbooks/$', polls_views.getbooks),

    # url()方法
    url(r'^add_two1/(\d+)/(\d+)/$', polls_views.add_two, name='urltest1'),
    # 自定义过滤器,匹配字母开头的任意字符串
    url(r'^customFilter/(\w.*)/$', polls_views.customFilter),

    ##==================== 20171221 20:21
    # 作业：建立一个图书列表页面，显示图书名列表，
    # 并实现点击书名跳转到图书详细页面，显示图书详细信息
    url(r'^booklist/$', polls_views.booklist),
    # 定义拼接地址，获取书籍信息
    url(r'^bookinfo/(\d+)/$', polls_views.bookinfo, name='bookinfo'),

    ##======================== 20171222 10:50
    ## 内置过滤器测试
    url(r'^filtertest/(.*)/$', polls_views.filter_test),

    ##======================== 20171222 10:50
    ## 利用表单增加图书，实现前台与数据库交互
    url(r'^addbook/$', polls_views.addbook),
    # 处理表单提交的数据，实现前台与数据库交互
    url(r'^addbooktodatabase/', polls_views.addbooktodatabase),
    # 添加成功后返回添加成功页面addok
    url(r'^addok/', polls_views.addok),

]


### 添加子应用app的路由
# 导入子应用app的路由文件（路由模块）
# from appName import urlsName
# 采用模块.变量的方式获取子应用的urls列表
# 将子应用的urls列表拼接到项目的urlpatterns列表
# urlpatterns = [ ... ] + urlsName.urls_list_name