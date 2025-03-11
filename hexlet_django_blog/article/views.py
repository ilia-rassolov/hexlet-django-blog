from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleCommentForm, ArticleForm


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

class CommentArticleView(View):

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_index')
        return render(request, 'article/show.html',
                      {'form': form, })

        # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        form = ArticleCommentForm() # Создаем экземпляр нашей формы
        return render(request, 'article/show.html',
                      {'form': form, 'article': article,}) # Передаем нашу форму в контексте

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles_index')

        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})

class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles_index')
