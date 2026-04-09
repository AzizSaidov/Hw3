from django.urls import path

from .views import *

urlpatterns = [
    path('products/', get_all_products),
    path('products/<int:pk>/', get_product),
    path('products/create/', create_productds),
    path('products/update/<int:pk>/', update_product),
    path('products/delete/<int:pk>/', delete_product),

    path('reviews/', get_reviews),
    path('reviews/create/', create_review),

]