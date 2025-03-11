from django import forms # Импортируем формы Django

from hexlet_django_blog.article.models import ArticleComment, Article

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['title', 'comment']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']