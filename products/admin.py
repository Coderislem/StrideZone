from django.contrib import admin
from .models import Product,Category,Product_img,Stock
# Register your models here.

admin.site.register(Product)
admin.site.register(Product_img)

admin.site.register(Category)
admin.site.register(Stock)
