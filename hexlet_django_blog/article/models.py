from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ArticleComment(models.Model):
    title = models.CharField('title', max_length=100)
    comment = models.CharField('comment', max_length=100)
