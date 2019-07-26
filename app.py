#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: app.py
Author: cyan
Time: 2019/7/26 10:36
Desc: 
"""
import time
from tasks import add

if __name__ == '__main__':
    print('start task...')
    result = add.delay(3, 5)
    print('end task...')
    print(result)
