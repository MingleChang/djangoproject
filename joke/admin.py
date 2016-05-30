# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import User,Category,Joke,Comment
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('account', 'status', 'ctime', 'mtime')
	list_filter = ('ctime',)
	search_fields = ('id', 'account')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', 'ctime', 'mtime')
	list_filter = ('ctime',)
	search_fields = ('id', 'title')

class JokeAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'status', 'ctime', 'mtime')
	list_filter = ('ctime',)
	search_fields = ('id', 'title', 'content')
class CommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'status', 'ctime', 'mtime')
	list_filter = ('ctime',)
	search_fields = ('id', 'content')
		

admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Joke,JokeAdmin)
admin.site,register(Comment,CommentAdmin)

