from django.urls import path
from .views import index, orderFun, delivery, delete

urlpatterns = [
    path('food/', index, name='index'),
    path('order/', orderFun, name='order'),
    path('delivery/', delivery, name='delivery'),
    path('delete/<int:id>', delete, name='delete')
]