from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from app.models import Product, Store, Category


# Create your views here.
def index(request):
    search = request.GET.get('search') or ''
    print(search)
    shops = Store.objects.filter(name__icontains=search)
    ctx = {
        'shops': shops
    }

    return render(request, 'app/index.html', context=ctx)


def add_store(request):
    print(request.POST.get('store_name'))
    store = Store()
    store.name = request.POST.get('store_name')
    store.slug = slugify(store.name, allow_unicode=True)
    store.save()
    return redirect('index')


def store(request, storeId):
    # {% url 'category' categoryId=category.id %}
    search = request.GET.get('search') or ''
    print(search)
    categories = Category.objects.filter(name__icontains=search)
    store = Store.objects.get(id=storeId)
    ctx = {
        'categories': categories,
        'store': store,
    }

    return render(request, 'app/store.html', context=ctx)


def add_category(request):
    category = Category()
    store = request.POST.get('store_name')
    category.name = request.POST.get('category_name')
    category.slug = slugify(category.name, allow_unicode=True)
    category.save()
    return redirect('store', storeId=store[0])


def delete_category(request):
    category_id = request.POST.get('category_id') or ''
    if category_id == '':
        return
    print(category_id)
    category = Category.objects.get(id=category_id)
    store = request.POST.get('store_name')
    category.delete()
    return redirect('store', storeId=store[0])


def update_category(request):
    store = request.POST.get('store_name')
    category_id = request.POST.get('category_id') or ''

    if category_id == '' or (not category_id.isdigit()):
        return redirect('store', storeId=store[0])
    category = get_object_or_404(Category, id=category_id)
    category.name = request.POST.get('category_name')
    category.slug = slugify(category.name, allow_unicode=True)
    category.save()
    return redirect('store', storeId=store[0])


def category(request, categoryId):
    search = request.GET.get('search') or ''
    print(search)
    products = Product.objects.filter(name__icontains=search, category=categoryId)
    category = Category.objects.get(id=categoryId)
    ctx = {
        'products': products,
        'category': category
    }
    return render(request, 'app/category.html', context=ctx)


def add_product(request):
    product = Product()
    category = request.POST.get('category_name')
    product.name = request.POST.get('product_name')
    print('asdsdfowkefpowekfowe')
    print(Category.objects.get(id=category[0]))
    product.price = request.POST.get('product_price')
    product.category = Category.objects.get(id=category[0])

    product.slug = slugify(product.name, allow_unicode=True)
    product.save()
    return redirect('category', categoryId=category[0])


def delete_product(request):
    product_id = request.POST.get('product_id') or ''
    if product_id == '':
        return
    print(product_id)
    product = Product.objects.get(id=product_id)
    category = request.POST.get('category_name')
    product.delete()
    return redirect('category', categoryId=category[0])


def update_product(request):
    category = request.POST.get('category_name')
    product_id = request.POST.get('product_id') or ''

    if product_id == '' or (not product_id.isdigit()):
        return redirect('category', categoryId=category[0])
    product = get_object_or_404(Product, id=product_id)
    product.name = request.POST.get('product_name')
    product.price = request.POST.get('product_price')
    product.slug = slugify(product.name, allow_unicode=True)
    product.save()
    return redirect('category', categoryId=category[0])
