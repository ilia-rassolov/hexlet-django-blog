from django.urls import path
import views
from hexlet_django_blog.article.views import IndexView


urlpatterns = [
    # path('', views.index),
    path('', IndexView.as_view(), name='index'),
]
