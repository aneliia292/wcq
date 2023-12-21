from django.shortcuts import render, redirect
from .forms import Food, Order
from .models import order, food

def index(request):
    Food = food.objects.all()
    return render(request, 'index.html', context={'Food':Food})

def orderFun(request):
    Order = order.objects.all()
    return render (request, 'order.html', context={'order': Order})


def delivery(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            food_delivery = form.cleaned_data['food_delivery']
            kolvo = form.cleaned_data['kolvo']
            price_delivery = form.cleaned_data['price_delivery']
            order.objects.create(food_delivery=food_delivery, kolvo=kolvo, price_delivery=price_delivery)
            return redirect('order')

    form = Order()
    return render (request, 'delivery.html', context={'form': form})

def delete(request, id):
    try:
        Order = order.objects.get(id=id)
        Order.delete()
        return redirect('order')
    except:
        return redirect('order')