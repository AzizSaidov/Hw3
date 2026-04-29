from django.urls import path

from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/update/<int:pk>/', ProductUpdateView.as_view()),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view()),

    path('reviews/', ReviewListView.as_view()),
    path('reviews/create/', ReviewCreateView.as_view()),

]
