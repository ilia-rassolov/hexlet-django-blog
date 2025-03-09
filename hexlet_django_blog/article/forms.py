from django import forms # Импортируем формы Django
from django.forms import ModelForm

from hexlet_django_blog.article.models import ArticleComment

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий', max_length=200) # Текст комментария

class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']