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
	account=models.CharField(unique=True,max_length=200, verbose_name='帐号')
	#密码
	password=models.CharField(max_length=200, verbose_name='密码')
	#昵称
	nickname=models.CharField(max_length=200,blank=True, verbose_name='昵称')
	#真实姓名
	realname=models.CharField(max_length=200,blank=True, verbose_name='真实姓名')
	#性别
	gender=models.IntegerField(null=True,blank=True, verbose_name='性别')
	#出生日期
	birthday=models.DateField(null=True,blank=True, verbose_name='出生日期')
	#出生时间
	birthtime=models.TimeField(null=True,blank=True, verbose_name='出生时间')
	#个人介绍
	introduction=models.CharField(max_length=1000,blank=True, verbose_name='个人介绍')
	#状态
	status=models.IntegerField(default=0, verbose_name='状态')
	#创建时间
	ctime=models.DateTimeField(auto_now=True, verbose_name='创建时间')
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

	def __unicode__(self):
		return self.account

#类别
class Category(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#分类名
	name=models.CharField( max_length=200, verbose_name='分类名')
	#状态
	status=models.IntegerField(default=0, verbose_name='状态')
	#创建时间
	ctime=models.DateTimeField(auto_now=True, verbose_name='创建时间')
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

	def __unicode__(self):
		return self.name
		
#内容
class Joke(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#标题
	title=models.CharField(max_length=500, verbose_name='标题')
	#内容
	content=models.TextField(verbose_name='内容')
	#作者
	author=models.ForeignKey(User,related_name='createjokes',verbose_name='作者')
	#类别
	category=models.ForeignKey(Category,related_name='jokes', verbose_name='类别')
	#点赞用户
	likes=models.ManyToManyField(User,related_name='likejokes', blank=True, verbose_name='点赞用户')
	#收藏用户
	collects=models.ManyToManyField(User,related_name='collectjokes', blank=True, verbose_name='收藏用户')
	#状态
	status=models.IntegerField(default=0, verbose_name='状态')
	#创建时间
	ctime=models.DateTimeField(auto_now=True, verbose_name='创建时间')
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

	def __unicode__(self):
		return self.content

	def toJsonValue(self):
		dic={'id':self.id.hex,
		'title':self.title,
		'content':self.content,
		'authorId':self.author.id.hex,
		'authorName':self.author.account}
		return dic

#评论
class Comment(models.Model):
	#id
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#评论详情
	content=models.TextField(verbose_name='评论详情')
	#评论人
	user=models.ForeignKey(User,related_name='comments', verbose_name='评论人')
	#被评论joke
	joke=models.ForeignKey(Joke,related_name='comments', verbose_name='被评论笑话')
	#状态
	status=models.IntegerField(default=0, verbose_name='状态')
	#创建时间
	ctime=models.DateTimeField(auto_now=True, verbose_name='创建时间')
	#最后修改时间
	mtime=models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

	def __unicode__(self):
		return self.content
		
		
		