from django.shortcuts import render, get_object_or_404
from django.db import models
from django.http import HttpResponse
from django.views import View

from hexlet_django_blog.article.models import Article, Comment
from hexlet_django_blog.article.forms import CommentArticleForm


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


# class ArticleCommentsView(View):
#
#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs['id'], article_id=kwargs['article_id'])
#         return None

class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данные формы на корректность
            comment = Comment(name = form.cleaned_data['content'],) # Получаем очищенные данные из поля content
            comment.save()                                          #  и создаем новый комментарий


    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):

        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form}) # Передаем нашу форму в контексте

