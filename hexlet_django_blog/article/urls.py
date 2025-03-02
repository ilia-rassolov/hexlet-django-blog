from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView


urlpatterns = [
    # path('', views.index),
    path('', IndexView.as_view(), name='index'),
]
