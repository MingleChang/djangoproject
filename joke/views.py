# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Category,Joke,Comment
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def test(request):
	name=request.GET.get('test','xxx')
	print name
	return HttpResponse(name)

@csrf_exempt
def categoryList(request):
	categoryList=[category.toJsonValue() for category in Category.objects.all()]
	return HttpResponse(json.dumps(categoryList))

@csrf_exempt
def jokeList(request):
	search=request.GET.get('search','')
	categoryId=request.GET.get('categoryId','')
	userId=request.GET.get('userId','')
	startIndex=request.GET.get('startIndex',0)
	pageCount=request.GET.get('pageCount',10)

	# jokes = null
	jokes=Joke.objects
	if userId != '':
		jokes=jokes.filter(author = userId)

	if search != '':
		jokes = jokes.filter(title__contains = search, content__contains = search)

	if categoryId != '':
		jokes = jokes.filter(category = categoryId)

	jokes=jokes[startIndex:pageCount]

	jokeList=[joke.toJsonValue() for joke in jokes.all()]
	return HttpResponse(json.dumps(jokeList))

def jokeDetail(request):
	jokeId=request.GET.get('jokeId','')
	
	if joke:
		return HttpResponse(json.dumps(joke.toJsonValue()))
	else:
		return HttpResponse('NONE')

def notFound(request):
	return HttpResponse('404')
