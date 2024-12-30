from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.display_cart, name='cart'),
    path('add-cart-item/<int:product_id>/', views.addCart_item, name='add_item'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('remove-item/<int:item_id>/', views.remove_cartitem, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('store/', views.store, name='store'),

]
