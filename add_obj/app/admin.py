from django.contrib import admin

from app.models import Store, Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", 'slug', 'price', 'category')
    search_fields = 'name',
    list_filter = 'name',


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", 'slug')
    search_fields = 'name',
    list_filter = 'name',


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", 'slug')
    search_fields = 'name',
    list_filter = 'name',


# Register your models here.
admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
