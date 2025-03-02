from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'Article',
#     })

class IndexView(View):


    template_name = "index.html"
    initkwargs = {'template_name': 'about.html'}

    def get(self, request, *args, **kwargs):
        return HttpResponse()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['who'] = 'Article'
    #     return context
