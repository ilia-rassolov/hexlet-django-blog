from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# def index(request):
#     return render(request, 'index.html',  context={
#         'who': 'Article',
#     })

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html',  context={
        'tags': 'python',
        'article_id': 42,
        })

