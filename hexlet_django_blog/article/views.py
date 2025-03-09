from django.shortcuts import render, get_object_or_404
from django.db import models
from django.http import HttpResponse

from hexlet_django_blog.article.models import Article, Comment
from django.views import View


# def index(request):
#     return render(request, 'index.html',  context={
#         'who': 'Article',
#     })

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })

class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article_id=kwargs['article_id'])

        return None

