from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, CommentArticleView


urlpatterns = [
    # path('', views.index),
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='show_article',),
    path('<int:id>/comment/', CommentArticleView.as_view(), name='comment_create',),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]
