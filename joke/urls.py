# -*- coding: UTF-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
	url(r'api/test$', views.test, name='test'),
	url(r'api/jokelist$', views.jokeList, name='jokeList'),
	url(r'api/jokedetail$', views.jokeDetail, name='jokeDetail'),
	url(r'api/categorylist$', views.categoryList, name='categoryList'),
=======
	url(r'api/jokelist', views.jokeList, name='jokeList'),
	url(r'api/jokedetail', views.jokeDetail, name='jokeDetail'),
	url(r'api/categorylist', views.categoryList, name='categoryList'),
>>>>>>> origin/master
	url(r'api/*', views.notFound, name='notFound'),
]