from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, Product_img
# Create your views here.


def women(request):
    products_women = Product.objects.filter(category__gender="women")
    categorys_women = Category.objects.filter(gender="women")
    context = {
        'products': products_women,
        'categories': categorys_women
    }
    return render(request, 'women.html', context)


def man(request):
    products_man = Product.objects.filter(category__gender="man")
    category_man = Category.objects.filter(gender="man")
    context = {
        'products': products_man,
        'categories': category_man
    }
    return render(request, 'men.html', context)


def search_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    else:
        products = []

    context = {
        'products': products,
        'query': query,
        'count': len(products)
    }
    return render(request, 'search_results.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Filter out product images that have no image file
    product_images = Product_img.objects.filter(
        product=product,
        product_image__isnull=False  # Changed from image to product_image
    ).exclude(product_image='')
    
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'product_images': product_images,
        'related_products': related_products,
    }
    return render(request, 'product-detail.html', context)