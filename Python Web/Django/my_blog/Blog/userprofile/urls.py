#!/usr/bin/python
# -*- coding: utf-8 --
#@File: urls.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/4/18 23:52

from django.urls import path, include
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path ('logout/', views.user_logout, name='logout'),
    # 用户注册
    path ('register/', views.user_register, name='register'),
    # 用户删除
    path ('delete/<int:id>/', views.user_delete, name='delete'),
]