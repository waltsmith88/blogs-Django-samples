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


    ##======================== 20171222 10:50
    ## 内置过滤器测试
    url(r'^filtertest/(.*)/$', polls_views.filter_test),




]

