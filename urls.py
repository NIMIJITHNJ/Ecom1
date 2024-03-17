
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home' ),
    path('products/',views.product_list, name='product_list'),
]