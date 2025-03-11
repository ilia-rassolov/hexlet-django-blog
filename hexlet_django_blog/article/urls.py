from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import (IndexView, ArticleView,
                                              CommentArticleView, ArticleFormEditView,
                                              ArticleFormDeleteView)


urlpatterns = [
    # path('', views.index),
    path('', IndexView.as_view(), name='articles_index'),
    # path('<int:id>/', ArticleView.as_view(), name='show_article',),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', CommentArticleView.as_view(), name='comment_create',),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]
