from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from hexlet_django_blog.products.models import Category, Product


# BEGIN (write your solution here)
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        current_category_id = kwargs.get('category_id')
        categories = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        context['current_category_id'] = current_category_id
        return context

    def get_queryset(self):
        current_category = self.kwargs.get('category_id')
        if current_category:
            products = Product.objects.filter(category__id=current_category).select_related('category')
        else:
            products = Product.objects.all()
        return products

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'product'

# END
