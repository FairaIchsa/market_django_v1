from django.db import models


class MenuCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Menu categories'

    name = models.CharField(max_length=255, verbose_name='Название категории')
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class SliderInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Slider info'

    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.URLField(verbose_name='Изображение')
    text = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = 'Subcategories'

    category = models.ForeignKey(Category, verbose_name='Категория', related_name='subcategories',
                                 on_delete=models.CASCADE)
    # или стоит привязать к продукту напрямую?
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{}: {}".format(self.category.name, self.name)


class Sale(models.Model):   # мб имеет смысл добавить поле name?
    class Meta:
        verbose_name_plural = 'Sales'

    is_active = models.BooleanField(default=True)
    sale_modifier = models.PositiveIntegerField(default=0)      # ограничить числом 100

    def __str__(self):
        return "{}%: {}".format(self.sale_modifier, "active" if self.is_active else "not active")


class Status(models.Model):
    class Meta:
        verbose_name_plural = 'Statuses'

    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Статус')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, verbose_name='Подкатегория', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Товаров на складе')
    sale = models.ForeignKey(Sale, verbose_name='Скидка', null=True, blank=True, on_delete=models.SET_NULL)
    is_popular = models.BooleanField(default=False)
    status = models.ForeignKey(Status, verbose_name='Статус', null=True, blank=True, on_delete=models.SET_NULL)
    # content = models.JSONField
    image = models.URLField(verbose_name='Основное изображение', null=True, blank=True)

    def __str__(self):
        return "{}: {}".format(self.category.name, self.name)


class SubImage(models.Model):
    class Meta:
        verbose_name_plural = 'Sub Images'

    product = models.ForeignKey(Product, verbose_name='Товар', related_name='images', on_delete=models.CASCADE)
    sub_image = models.URLField(verbose_name='Дополнительное изображение', null=True, blank=True)

    def __str__(self):
        return "SubImage {} for {}".format(self.id, self.product)


# class ChildProductData(models.Model):
#     class Meta:
#         abstract = True
#
#     product = models.OneToOneField(Product, verbose_name='Товар', related_name='child_product_data',
#                                    on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.product.category.name}: {self.product.name}"
#
#
# class Ball(ChildProductData):
#     class Meta:
#         verbose_name_plural = 'Balls'
#
#     size = models.PositiveIntegerField(verbose_name='Размер')
#
#
# class TennisTable(ChildProductData):
#     class Meta:
#         verbose_name_plural = 'Tennis tables'
#
#     foldable = models.BooleanField(default=False, verbose_name='Складной')
#     folded_size = models.CharField(max_length=255, verbose_name='Размер в сложенном состоянии')
#     unfolded_size = models.CharField(max_length=255, verbose_name='Размер в разложенном состоянии')
