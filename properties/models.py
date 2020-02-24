from django.db import models
# from products.models import Product
# from products.models import Category
# Create your models here.
class CategoryProperty(models.Model):
    name = models.CharField(blank=True,max_length=250,unique=True)
    category = models.ForeignKey('products.Category',on_delete=models.CASCADE,related_name='categories_property',verbose_name ='Category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category property'
        verbose_name_plural = 'Category properties'



class ProductProperty( models.Model):
    category_property = models.ForeignKey(CategoryProperty,on_delete=models.CASCADE,null=True,blank=True,related_name='category_property',verbose_name ='Propery',to_field='name')
    value = models.CharField(default="",max_length=250)
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,related_name='properties_product',verbose_name ='Product')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Product property'
        verbose_name_plural = 'Product properties'
