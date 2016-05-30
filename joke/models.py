# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime,uuid
# Create your models here.

#用户
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
	#状态
	status=models.IntegerField(default=0)
	#创建时间
	ctime=models.DateTimeField(auto_now=True)
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.account

#类别
class Category(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#分类名
	name=models.CharField(max_length=200)
	#状态
	status=models.IntegerField(default=0)
	#创建时间
	ctime=models.DateTimeField(auto_now=True)
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name
		
#内容
class Joke(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#标题
	title=models.CharField(max_length=500)
	#内容
	content=models.TextField()
	#作者
	author=models.ForeignKey(User,related_name='createjokes')
	#类别
	category=models.ForeignKey(Category,related_name='jokes')
	#点赞用户
	likes=models.ManyToManyField(User,related_name='likejokes',null=True)
	#收藏用户
	collects=models.ManyToManyField(User,related_name='collectjokes',null=True)
	#状态
	status=models.IntegerField(default=0)
	#创建时间
	ctime=models.DateTimeField(auto_now=True)
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.content

#评论
class Comment(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#评论详情
	content=models.TextField()
	#评论人
	user=models.ForeignKey(User,related_name='comments')
	#被评论joke
	joke=models.ForeignKey(Joke,related_name='comments')
	#状态
	status=models.IntegerField(default=0)
	#创建时间
	ctime=models.DateTimeField(auto_now=True)
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content
		
		
		