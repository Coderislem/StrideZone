from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from products.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_cart")
    total_price = models.IntegerField( default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Cart-{self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_item")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_cart")
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    def __str__(self):
        return self.product.name
    


