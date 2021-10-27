from django.db import models


class MenuCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Menu categories'

    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class SliderInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Slider info'

    img = models.ImageField(verbose_name='Изображение')
    main = models.CharField(max_length=255)
    base = models.CharField(max_length=255)
    text_1_main = models.CharField(max_length=255, null=True, blank=True)
    text_1_base = models.CharField(max_length=255, null=True, blank=True)
    text_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Текст 2')
    text_3_main = models.CharField(max_length=255, null=True, blank=True)
    text_3_base = models.CharField(max_length=255, null=True, blank=True)
    text_4 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Текст 4')

    def __str__(self):
        return f"slider { self.id }"
