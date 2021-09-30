from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Sale)
admin.site.register(Status)
admin.site.register(Product)
