from .models import Cart

def cart_processor(request):
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            # Use annotate to get the correct count
            cart_count = cart.cart_item.all().count()
        except Cart.DoesNotExist:
            cart_count = 0
    return {'cart_count': cart_count}
