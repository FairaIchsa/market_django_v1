from django.db import models


class MenuCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Menu categories'

    name = models.CharField(max_length=255, verbose_name='Название категории')
    url = models.URLField(unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name


class SliderInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Slider info'

    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.URLField(verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст')

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

    category = models.ForeignKey(Category, verbose_name='Категория', related_name='product', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, verbose_name='Подкатегория', on_delete=models.CASCADE,
                                    blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Товаров на складе')
    sale = models.ForeignKey(Sale, verbose_name='Скидка', null=True, blank=True, on_delete=models.SET_NULL)
    is_popular = models.BooleanField(default=False, verbose_name='Популярен')
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


class Ball(models.Model):
    class Meta:
        verbose_name_plural = 'Balls'

    product = models.OneToOneField(Product, verbose_name='Товар', related_name='child_product_ball',
                                   on_delete=models.CASCADE)
    size = models.PositiveIntegerField(verbose_name='Размер')

    def __str__(self):
        return f"{self.product} additional info"


class TennisTable(models.Model):
    class Meta:
        verbose_name_plural = 'Tennis tables'

    product = models.OneToOneField(Product, verbose_name='Товар', related_name='child_product_tennis_table',
                                   on_delete=models.CASCADE)
    foldable = models.BooleanField(default=False, verbose_name='Складной')
    folded_size = models.CharField(max_length=255, verbose_name='Размер в сложенном состоянии',
                                   blank=True, null=True)
    unfolded_size = models.CharField(max_length=255, verbose_name='Размер в разложенном состоянии')

    def __str__(self):
        return f"{self.product} additional info"
