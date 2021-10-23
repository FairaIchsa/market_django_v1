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

    image = models.ImageField(verbose_name='Изображение')
    header = models.TextField(verbose_name='Заголовок')
    base = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return f"slider { self.id }"


class SliderText(models.Model):
    slider = models.ForeignKey(SliderInfo, verbose_name='Слайдер', related_name='content', on_delete=models.CASCADE)
    main = models.TextField(verbose_name='Подзаголовок')
    base = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return f"content {self.id} for {self.slider}"

