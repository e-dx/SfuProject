from django.db import models


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
        verbose_name_plural = "Поставщик"
        
        
class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    deliveryDate = models.DateTimeField("Дата поставки")
    deliveryCost = models.FloatField("Цена поставки")
    productCountOnWh = models.IntegerField("Количество на складе")
    
    def __str__(self):
        return f"{self.product} - {self.vendor} - {self.productCountOnWh} шт."

    class Meta:
        verbose_name_plural = "Склад"