# coding:utf-8

from __future__ import unicode_literals

from django.db import models
from mongoengine import *

class Tourist(Document):
    id = IntField()           # 站点id
    status = StringField()    # 状态 默认为1 在抓取， 不在抓取0
    tourist_id = IntField()   # 景点id
    task_id = IntField()      # 任务id
    task_name = StringField() # 任务名称
    crawler_name = StringField() #爬虫名字
    crawler_url = StringField() # 爬去的url
    last_time = DateTimeField() # 上次抓取时间
    crawler_grades = IntField() # 抓去等级
    crawler_status = StringField() # 抓取状态 1 在抓取，-1 停止
    lock_status = StringField()  # 是否锁定
    lock_time = IntField() # 锁定时间
    # test_key = StringField(required=True)
    # test_value = StringField(max_length=50)

