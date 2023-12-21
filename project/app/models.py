from django.db import models

class food(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10000)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class category(models.Model):
    name_category = models.CharField(max_length=20)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class order(models.Model):
    food_delivery = models.CharField(max_length=100)
    kolvo = models.IntegerField(max_length=100000)
    price_delivery = models.IntegerField(max_length=1000)

    def __str__(self):
        return self.food_delivery

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
