from django.db import models


# Create your models here.


# 定义心情记录
class Mood(models.Model):
    '''记录心情内容'''
    mood_title = models.CharField(max_length=20)  # 内容标题
    mood_time = models.CharField(max_length=20)  # 更新时间
    mood_content = models.CharField(max_length=128, default='开心的很，没有要讲的')  # 内容主体

    def __str__(self):
        '''返回标题名'''
        return self.mood_title


# 定义文章栏目
class Column(models.Model):
    '''文章栏目'''
    column_name = models.CharField(max_length=20)


# 定义文章属性
class Article(models.Model):
    '''记录文章相关内容'''
    title = models.CharField(max_length=50)  # 主标题
    pub_date = models.CharField(max_length=20)  # 上传时间
    editor = models.CharField(max_length=20)  # 作者
    summary = models.CharField(max_length=200)  # 文章概要
    content = models.TextField(max_length=5000)  # 文章内容
    key_word1 = models.CharField(max_length=20)  # 关键词1
    key_word2 = models.CharField(max_length=20)  # 关键词2
    key_word3 = models.CharField(max_length=20)  # 关键词3
    article_column = models.ForeignKey('Column', on_delete=models.CASCADE)  # 关联文章栏目
