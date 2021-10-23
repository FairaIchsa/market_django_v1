from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *
from .product_models import *
from .other_models import *


class BallAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product':
            return ModelChoiceField(Product.objects.filter(category_id=Category.objects.get(slug='balls')))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TennisTableAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product':
            return ModelChoiceField(Product.objects.filter(category_id=Category.objects.get(slug='tennis_tables')))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Description)
admin.site.register(SubImage)
admin.site.register(MenuCategory)
admin.site.register(SliderInfo)
admin.site.register(SliderText)
admin.site.register(Ball, BallAdmin)
admin.site.register(TennisTable, TennisTableAdmin)

