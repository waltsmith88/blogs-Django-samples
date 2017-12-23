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


    # 并实现点击书名跳转到图书详细页面，显示图书详细信息
    url(r'^booklist/$', polls_views.booklist),
    # 定义拼接地址，获取书籍信息
    url(r'^bookinfo/(\d+)/$', polls_views.bookinfo, name='bookinfo'),

    ##======================== 20171222 10:50
    ## 利用表单增加图书，实现前台与数据库交互
    url(r'^addbook/$', polls_views.addbook),
    # 处理表单提交的数据，实现前台与数据库交互
    url(r'^addbooktodatabase/', polls_views.addbooktodatabase),
    # 添加成功后返回添加成功页面addok
    url(r'^addok/', polls_views.addok),

]
