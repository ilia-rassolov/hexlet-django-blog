from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Category, Product


# BEGIN (write your solution here)
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        current_category_id = kwargs.get('category_id')
        if current_category_id:
            current_category = get_object_or_404(Category, id=current_category_id)
            products = Product.objects.filter(category=current_category)
        else:
            products = Product.objects.all()
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['products'] = products
        context['current_category_id'] = current_category_id
        context['categories'] = categories
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'product'

# END
