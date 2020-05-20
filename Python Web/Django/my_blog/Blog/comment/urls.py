#!/usr/bin/python
# -*- coding: utf-8 --
#@File: urls.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/4/19 13:51

from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]