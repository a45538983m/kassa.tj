from django.db import models

class Product(models.Model):

    nameproduct = models.CharField("Названые продукта", max_length=100)
    address = models.IntegerField("Код продукта")

    class Meta: 
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.clientname