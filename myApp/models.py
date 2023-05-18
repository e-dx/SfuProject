from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание товара')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Товар"
        
        
class Vendor(models.Model):
    title = models.CharField('Название компании', max_length=200)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Поставщики"
        
        
class Warehouse(models.Model):
    product = models.ForeignKey(to=Product, verbose_name="Товар", on_delete=models.CASCADE)
    vendor = models.ForeignKey(to=Vendor, verbose_name="Поставщик", on_delete=models.CASCADE)
    deliveryDate = models.DateTimeField("Дата поставки")
    deliveryCost = models.FloatField("Цена поставки")
    productCountOnWh = models.IntegerField("Количество на складе")
    
    def __str__(self):
        return f"{self.product} - {self.vendor} - {self.productCountOnWh} шт."

    class Meta:
        verbose_name_plural = "Склад"
        

class Trade(models.Model):
    date = models.DateTimeField("Дата сделки")
    product = models.ForeignKey(to=Product, verbose_name="Товар", on_delete=models.CASCADE)
    count = models.IntegerField("Количество")
    costPerOne = models.FloatField("Цена за единицу")
    manager = models.ForeignKey(to=User, verbose_name="Менеджер", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.manager} - {self.product} - {self.count} шт."

    class Meta:
        verbose_name_plural = "Сделки"