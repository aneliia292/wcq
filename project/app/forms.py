from django import forms

class Food(forms.Form):
    name = forms.CharField(label='Название блюда')
    about = forms.CharField (label='Состав')
    price = forms.CharField (label='Цена')
    category = forms.CharField (label='Категория')

class Category(forms.Form):
    name_category = forms.CharField(label='Категория')

class Order(forms.Form):
    food_delivery = forms.CharField(label='Блюдо')
    kolvo = forms.IntegerField(label='Количество')
    price_delivery = forms.IntegerField(label='Цена')