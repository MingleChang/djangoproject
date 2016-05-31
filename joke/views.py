# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Category,Joke,Comment
import json
# Create your views here.

def test(request):
	name=request.GET.get('test','xxx')
	print name
	return HttpResponse(name)

def jokeList(request):
	# search=request.POST.get('search','')
	# categoryId=request.POST.get('categoryid','')
	jokeList=Joke.objects.get(pk='a0bc76bc-e762-427c-a4a6-718854f20b8e')
	return HttpResponse(json.dumps(jokeList.toJsonValue()))

def notFound(request):
	return HttpResponse('404')
