#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2017-12-20

import os
import django
from polls.models import Person
# 设置Django的环境设置参数
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")# project_name 项目名称
django.setup()

