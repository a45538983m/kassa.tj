
from django.db import models


class Product(models.Model):

    nameproduct = models.CharField(
        "Название продукта",
        max_length=100
    )

    code = models.IntegerField("Код продукта", unique=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.nameproduct


class Overhead(models.Model):

    nameover = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="overheads"
    )

    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2
    )

    quantity = models.FloatField("Количество")

    class Meta:
        verbose_name = "Накладная"
        verbose_name_plural = "Накладные"

    def __str__(self):
        return self.nameover.nameproduct


class Warehouse(models.Model):

    namewar = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="warehouse_records"
    )

    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2
    )

    remainder = models.FloatField("Остаток")

    class Meta:
        verbose_name = "Остаток"
        verbose_name_plural = "Остатки"

    def __str__(self):
        return self.namewar.nameproduct
