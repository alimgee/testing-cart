from django.urls import path, include
from django.conf.urls import url

from cart.views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<pk>/', add_to_cart, name='add_to_cart'),
    #url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    path('adjust/<int:pk>/', adjust_cart, name='adjust_cart'),
]