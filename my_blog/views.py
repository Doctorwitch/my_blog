from django.shortcuts import render
from my_blog.models import Mood, Article, Column

# Create your views here.

# /index
def index(request):
    '''定义首页'''
    return render(request, 'my_blog/index.html')


# /about
def about(request):
    '''定义个人信息'''
    return render(request, 'my_blog/about.html')


# /article
def article(request):
    '''定义个人信息'''
    article = Article.objects.all()
    column = Article.article_column
    return render(request, 'my_blog/article.html', {'article': article, 'column': column})


# /article_detail
def article_detail(request, num):
    '''定义个人信息'''
    article = Article.objects.get(id=num)
    return render(request, 'my_blog/article_detail.html', {'article': article})


# /board
def board(request):
    '''定义个人信息'''
    return render(request, 'my_blog/board.html')


# /mood
def mood(request):
    '''定义个人信息'''
    moods = Mood.objects.all()
    return render(request, 'my_blog/mood.html', {'moods': moods})


def page_not_found(request):
    return render(request, 'my_blog/404.html')












