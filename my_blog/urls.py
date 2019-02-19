from django.conf.urls import url
from my_blog import views

urlpatterns = [
    # 主要页面
    url(r'^index$', views.index),
    url(r'^about$', views.about),
    url(r'^article$', views.article),
    # url(r'^article_detail$', views.article_detail),
    url(r'^board$', views.board),
    url(r'^mood$', views.mood),

    # 文章内容页
    url(r'^article_detail/(?P<num>\d+)$', views.article_detail)
]

handler404 = views.page_not_found
