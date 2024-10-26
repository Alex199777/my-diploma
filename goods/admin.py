from django.contrib import admin
from .models import Category, Product
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}#Передаем данные которые должны отображаться автоматически, вторым параметром передаем откуда слаг должен брать пример

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}