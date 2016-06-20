# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Category,Joke,Comment
from django.views.decorators.csrf import csrf_exempt
import json,uuid
import utility
# Create your views here.

@csrf_exempt
def categoryList(request):
	categoryList=[category.toJsonValue() for category in Category.objects.all()]
<<<<<<< HEAD
	result=utility.apiJson(status=200,data=categoryList)
	return HttpResponse(result)
=======
	try:
		result=utility.apiJson(status=utility.CODE_SUCCESS,data=categoryList)
	except Exception, e:
		result=utility.apiJson(status=utility.CODE_SERVER_ERROR,message='服务器异常')
		return HttpResponse(result)
	else:
		return HttpResponse(result)
>>>>>>> origin/master

# Joke列表的api
@csrf_exempt
def jokeList(request):
	search=request.GET.get('search','')
	categoryId=request.GET.get('categoryId','')
	userId=request.GET.get('userId','')
	startIndex=request.GET.get('startIndex',0)
	pageCount=request.GET.get('pageCount',10)

	jokes=Joke.objects

	#根据joke的作者搜索，如果userId为空，则搜索所有
	if userId != '':
		try:
			uuid.UUID(userId)
		except Exception, e:
<<<<<<< HEAD
			return HttpResponse(utility.apiJson(status=300,message='UserId格式错误'))
=======
			result=utility.apiJson(status=utility.CODE_PARAM_ERROR,message='UserId格式错误')
			return HttpResponse(result)
>>>>>>> origin/master
		jokes=jokes.filter(author = userId)

	if search != '':
		jokes = jokes.filter(title__contains = search, content__contains = search)

	#根据joke的类型搜索，如果categoryId为空，则搜索所有
	if categoryId != '':
		try:
			uuid.UUID(categoryId)
		except Exception, e:
<<<<<<< HEAD
			return HttpResponse(utility.apiJson(status=300,message='categoryId格式错误'))
=======
			result=utility.apiJson(status=utility.CODE_PARAM_ERROR,message='categoryId格式错误')
			return HttpResponse(result)
>>>>>>> origin/master
		jokes = jokes.filter(category = categoryId)

	#分页处理
	jokes=jokes.all()[startIndex:pageCount]

	try:
		jokeList=[joke.toJsonValue() for joke in jokes]
		result=utility.apiJson(status=utility.CODE_SUCCESS,data=jokeList)
	except Exception, e:
<<<<<<< HEAD
		return HttpResponse(utility.apiJson(status=500))
	else:
		return HttpResponse(utility.apiJson(status=200,data=jokeList))
	
=======
		result=utility.apiJson(status=utility.CODE_SERVER_ERROR,message='服务器异常')
		return HttpResponse(result)
	else:
		return HttpResponse(result)
>>>>>>> origin/master

#joke详情
@csrf_exempt
def jokeDetail(request):
	jokeId=request.GET.get('jokeId','')
	#根据
	if jokeId == '':
		result=utility.apiJson(status=utility.CODE_PARAM_ERROR,message='jokeId不能为空')
		return HttpResponse(result)
	else:
		try:
			uuid.UUID(jokeId)
		except Exception, e:
			result=utility.apiJson(status=utility.CODE_PARAM_ERROR,message='jokeId格式错误')
			return HttpResponse(result)
	try:
		joke=Joke.objects.get(pk=jokeId)
	except Exception, e:
		result=utility.apiJson(status=utility.CODE_DATA_ERROR,message='该Joke不存在')
		return HttpResponse(result)
	else:
		result=utility.apiJson(status=utility.CODE_SUCCESS,data=joke.toJsonValue())
		return HttpResponse(result)

def notFound(request):
<<<<<<< HEAD
	return HttpResponse(utility.apiJson())
=======
	result=utility.apiJson(status=utility.CODE_NOT_FOUND,message='该接口不存在')
	return HttpResponse(result)
>>>>>>> origin/master
