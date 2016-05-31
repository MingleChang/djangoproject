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
	search=request.POST.get('search','')
	categoryId=request.POST.get('categoryId','')
	userId=request.POST.get('userId','')
	startIndex=request.POST.get('startIndex',0)
	pageCount=request.POST.get('pageCount',10)

	jokeList=[joke.toJsonValue() for joke in Joke.objects.all()]
	return HttpResponse(json.dumps(jokeList))

def notFound(request):
	return HttpResponse('404')
