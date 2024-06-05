from django.urls import path

from app.views import index, add_store, store, add_category, delete_category, update_category, category, add_product, \
    delete_product, update_product

urlpatterns = [
    path('', index, name='index'),
    path('add', add_store),
    path('add_category', add_category),
    path('add_product', add_product),
    path('delete_category', delete_category),
    path('delete_product', delete_product),
    path('update_category', update_category),
    path('update_product', update_product),
    path('store/<int:storeId>', store, name='store'),
    path('category/<int:categoryId>', category, name='category'),

]
