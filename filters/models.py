from django.db import models
# from products.models import Product
# from products.models import Category
# from slugify import slugify



class FilterCategory(models.Model):
    category = models.ForeignKey('products.Category',on_delete=models.CASCADE,related_name='filtercategories',verbose_name ='Category')
    slug = models.CharField(default="",blank=True,max_length=250)
    # name = models.CharField(blank=True,max_length=250,unique=True)
    name = models.CharField(blank=True,max_length=250)

    def __str__(self):
        return self.name

    # def save(self):
    #     if not self.slug:
    #         self.slug = slugify(self.name)

        # super(FilterCategory, self).save()

    class Meta:
        verbose_name = 'Filter Category'
        verbose_name_plural = 'Filters Category'



class FilterSelect(models.Model):
    category = models.ForeignKey('products.Category',null=True,on_delete=models.CASCADE,verbose_name ='Категория',to_field='name')
    # filter_category = models.ForeignKey(FilterCategory,on_delete=models.CASCADE,verbose_name ='Filter Category',to_field='name')
    # category = models.ForeignKey('products.Category',null=True,on_delete=models.CASCADE,verbose_name ='Категория')
    filter_category = models.ForeignKey(FilterCategory,on_delete=models.CASCADE,verbose_name ='Filter Category')
    slug = models.CharField(default="",blank=True,max_length=250)
    url = models.CharField(default="",blank=True,max_length=250)
    # name = models.CharField(unique=True,blank=True,max_length=250)
    name = models.CharField(blank=True,max_length=250)
    simple = models.CharField(blank=True,max_length=250)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Filter Select'
        verbose_name_plural = 'Filters Select'



class ProductFilter(models.Model):
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,related_name='filterproducts',null=True,verbose_name ='Product')
    # filter_category = models.ForeignKey(FilterCategory,on_delete=models.CASCADE,null=True,related_name='filter_select_product',verbose_name ='Filter Category',to_field='name')
    # values = models.ForeignKey(FilterSelect,on_delete=models.CASCADE,related_name='filtervalues',null=True,blank=True,verbose_name ='Values',to_field='name')
    filter_category = models.ForeignKey(FilterCategory,on_delete=models.CASCADE,null=True,related_name='filter_select_product',verbose_name ='Filter Category')
    values = models.ForeignKey(FilterSelect,on_delete=models.CASCADE,related_name='filtervalues',null=True,blank=True,verbose_name ='Values')
    # values = models.ManyToManyField(FilterSelect,related_name='filtervalues',blank=True,verbose_name ='Values')
    simple = models.CharField(blank=True,max_length=250)
    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Product Filter'
        verbose_name_plural = 'Product Filters'
