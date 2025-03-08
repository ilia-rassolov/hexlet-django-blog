from django.shortcuts import render
from django.db import models
from django.http import HttpResponse

from hexlet_django_blog.article.models import Article
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

