#!/usr/bin/python
# -*- coding: utf-8 --
#@File: forms.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/4/19 13:51

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']