#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2017-12-21

from django.http import HttpResponse
from django import template
# 注册过滤器
register = template.Library()

@register.filter    #装饰器形式注册自定义过滤器
def removetags(value, arg):
    # value = '<p>a</p><b>ddd</b>'
    # arg='p b'
    # 1.把arg变成列表
    arg_list = arg.split()
    # 2.遍历列表，对value执行字符串替换
    for tag in arg_list:
        value = value.replace(tag, '')
    #<>a</><>ddd</>
    value = value.replace('<>', '')
    value = value.replace('</>', '')
    # 3.返回value
    return value

# 注册这个自定义过滤器
#register.filter(name='removetags',filter_func=removetags)
