#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: tasks.py
Author: cyan
Time: 2019/7/26 10:47
Desc: 
"""
import time
from celery import Celery

broker = 'redis://192.168.0.8:16379/1'  # redis消息中间件
backend = 'redis://192.168.0.8:16379/2'  # 重置任务执行结果
app = Celery('my_task', broker=broker, backend=backend)  # 实例化一个celery


@app.task  # 给add方法加上一个装饰器，这样add方法就变成异步的了
def add(x, y):
    print('enter call func...')
    time.sleep(4)
    return x + y
