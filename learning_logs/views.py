# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Topic   # 需要从Topic模型中获取数据进行显示
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """显示网站中记录的所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """显示特定主题的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

