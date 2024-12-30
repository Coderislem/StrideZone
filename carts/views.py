from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from products.models import Product

@login_required
def addCart_item(request, product_id):
    try:
        # Get or create cart for user
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Get product
        product = Product.objects.get(id=product_id)
        
        try:
            # Try to get existing cart item
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += 1
            cart_item.price = product.real_price * cart_item.quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            # Create new cart item
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=1,
                price=product.real_price
            )
        
        # Update cart total
        cart.total_price = sum(item.price for item in cart.cart_item.all())
        cart.save()
            
        return redirect('man')  # Changed from 'man' to 'men' assuming that's your URL name
        
    except Exception as e:
        print(f"Error adding item to cart: {e}")
        return redirect('man')
    



@login_required
def update_cart(request):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity'))
            
            cart = Cart.objects.get(user=request.user)
            product = Product.objects.get(id=product_id)
            cart_item = CartItem.objects.get(cart=cart, product=product)
            
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.price = product.real_price * quantity
                cart_item.save()
                
                # Update cart total
                cart.total_price = sum(item.price for item in cart.cart_item.all())
                cart.save()
                messages.success(request, 'Cart updated successfully!')
            else:
                cart_item.delete()
                messages.warning(request, 'Item removed from cart!')
                
        except Exception as e:
            messages.error(request, 'Error updating cart!')
            print(f"Error updating cart: {e}")
            
    return redirect('cart')

@login_required
def display_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cart_item.all()
        total = cart.total_price
        context = {
            'cart_items': cart_items,
            'total': total
        }
    except Cart.DoesNotExist:
        context = {
            'cart_items': None,
            'total': 0
        }
    return render(request, 'carts/cart.html', context)

@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        if cart.cart_item.count() > 0:
            return render(request, 'carts/checkout.html', {
                'cart': cart,
                'cart_items': cart.cart_item.all(),
                'total': cart.total_price
            })
        else:
            messages.warning(request, 'Your cart is empty!')
            return redirect('cart')
    except Cart.DoesNotExist:
        messages.error(request, 'No cart found!')
        return redirect('store')

def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})

def display_Cartitems(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_item.all()
    return render(request, 'carts/cart.html', {'cart_items': cart_items})

def remove_cartitem(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return redirect('cart')
    except Exception as e:
        print(f"Error removing item from cart: {e}")
        return redirect('cart')