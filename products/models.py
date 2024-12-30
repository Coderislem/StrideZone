from django.db import models

# Create your models here.

class Category(models.Model):
    class genderType(models.TextChoices):
        man = 'man','Man'
        women = 'women','Women'
    
    name = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField()
    gender = models.CharField(
        choices=genderType.choices,
        default=genderType.man,
        max_length=10

    )
    image_category = models.ImageField(upload_to="categorys/",blank=True,null=True)
    def __str__(self):
        return f"{self.name} - {self.get_gender_display()}"

# class Product_category(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_category')
#     category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_product')


class Product(models.Model):
    name = models.CharField(max_length=100,blank=True)
    fake_price = models.CharField(max_length=15,blank=True)
    real_price = models.CharField(max_length=15,blank=True)
    description = models.TextField(blank=True,null=True)
    brand = models.CharField(null=True,blank=True,max_length=20)
    image = models.ImageField(upload_to='product_imgs/', blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    def __str__(self):

        return f'Product {self.name}'

class Product_img(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_imgs')
    product_image = models.ImageField(blank=True,upload_to="product_imgs/",null=True)
    def __str__(self):
        return f'img for {self.product}'


class Stock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_stock')
    Quantity = models.IntegerField()
    def __str__(self):
        return f'{self.product}-{self.Quantity}'


