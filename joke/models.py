# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime,uuid
# Create your models here.

class User(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#帐号
	account=models.CharField(unique=True,max_length=200)
	#密码
	password=models.CharField(max_length=200)
	#昵称
	nickname=models.CharField(max_length=200,blank=True)
	#真实姓名
	realname=models.CharField(max_length=200,blank=True)
	#性别
	gender=models.IntegerField(null=True,blank=True)
	#出生日期
	birthday=models.DateField(null=True,blank=True)
	#出生时间
	birthtime=models.TimeField(null=True,blank=True)
	#个人介绍
	introduction=models.CharField(max_length=1000,blank=True)
	#创建时间
	ctime=models.DateTimeField(auto_now=True)
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.account

class Joke(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#标题
	title=models.CharField(max_length=500)
	#内容
	content=models.TextField()
	#作者
	author=models.ForeignKey(User)

	def __unicode__(self):
		return self.content

		
		