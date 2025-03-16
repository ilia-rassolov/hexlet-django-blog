from django.urls import path

from hexlet_django_blog.products.views import ProductDetailView, ProductListView

# BEGIN (write your solution here)
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='product_by_category'),
    path('<int:id>/', ProductDetailView.as_view(), name='product_detail'),
]
# END