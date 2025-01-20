from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, Product_img
import os
from django.contrib.auth.decorators import login_required
from carts.models import Cart
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
    product_images = Product_img.objects.filter(product=product).all()
    
    # Enhanced debugging
    print("\n=== Debug Information ===")
    print(f"Product ID: {product_id}")
    print(f"Product Name: {product.name}")
    print(f"Main Product Image: {product.image.url if product.image else 'No main image'}")
    print("\nProduct Additional Images:")
    for img in product_images:
        try:
            print(f"- Image ID: {img.id}")
            print(f"- Image URL: {img.product_image.url}")
            print(f"- Image Path: {img.product_image.path}")
            print("---")
        except Exception as e:
            print(f"Error with image: {str(e)}")
    
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'product_images': product_images,
        'related_products': related_products,
        'DEBUG': True  # Add this for template debugging
    }
    return render(request, 'product-detail.html', context)


@login_required
def payment_view(request):
    cart = Cart.objects.get(user=request.user)
    context = {
        'cart': cart,
        'total': cart.total_price
    }
    return render(request, 'payment.html', context)