from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'Article',
#     })

class IndexView(View):

    template_name = "index.html"
    context = {'who': 'Article', }

    def get(self, request, *args, **kwargs):
        return HttpResponse()
