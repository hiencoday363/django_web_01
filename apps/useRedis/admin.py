from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'country')


@admin.register(CarDetail)
class CarDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
