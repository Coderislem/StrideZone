from django.contrib.auth.models import User
from carts.models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
@receiver(post_save,sender=User)
def create_cart_for_user(sender,instance,created,**kwargs):
    if created:
        Cart.objects.create(user=instance)
        print("cart created !")
    else:
        print("cart not created !")
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile created !")
    else:
        print("profile not created !")