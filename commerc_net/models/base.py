from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    product = models.ManyToManyField('Product')
    debt = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)


class Address(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title}, {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'