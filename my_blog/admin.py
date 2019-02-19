from django.contrib import admin
from my_blog.models import Mood

# Register your models here.

class MoodAdmin(admin.ModelAdmin):
    '''心情模型管理类'''
    list_display = ['id', 'mood_title', 'mood_time', 'mood_content']

# 注册心情模型类
admin.site.register(Mood, MoodAdmin)
