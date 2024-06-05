from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return f"{self.id}. {self.name}"

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.name}'

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'
        ordering = ['id']


class Store(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    products = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return f'{self.id}. {self.name}'

    class Meta:
        verbose_name_plural = 'Магазины'
        verbose_name = 'Магазин'
        ordering = ['id']
