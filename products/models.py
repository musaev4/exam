from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    content = models.TextField(verbose_name='Контент')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product',
                                 verbose_name='категория')
    tags = models.ManyToManyField('Tag', related_name='news', verbose_name='теги', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField(upload_to='product_images', verbose_name='Фото')


class ProductAttribute(models.Model):
    class Meta:
        verbose_name = 'атрибут продукта'
        verbose_name_plural = 'атрибуты продуктов'

    key = models.CharField(verbose_name='название', max_length=100)
    value = models.CharField(verbose_name='значение', max_length=100)
    link = models.URLField(verbose_name='ссылка', null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes', verbose_name='продукт')


class Tag(models.Model):
    name = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
