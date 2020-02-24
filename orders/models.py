
from django.db import models
from products.models import Product
from django.db.models.signals import post_save
# место где хронится пользователь
from django.contrib.auth.models import User

# ----------------------------------STATUS--------------------------------------------------------------
class Status(models.Model):
    name = models.CharField(max_length=24,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    # вывод одного поля
    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'
# ---------------------------------- END STATUS--------------------------------------------------------------

# ----------------------------------ORDRE--------------------------------------------------------------
class Order(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, default=None,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0)#total price for all products in order
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_surname = models.CharField(max_length=120,blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=120,blank=True, null=True, default=None)
    customer_tel = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_city = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_street = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    token = models.CharField(max_length=128,blank=True, null=True, default=None)
    # productinorder = models.ForeignKey(ProductInOrder, blank=True, null=True, default=None)
    # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id )
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

         super(Order, self).save(*args, **kwargs)
# ----------------------------------END ORDRE--------------------------------------------------------------

# ----------------------------------PRODUCT IN ORDRE--------------------------------------------------------------
class ProductInOrder(models.Model):
    order = models.ForeignKey(Order,blank=True, null=True, default=None,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0)#price*nmb
    # customer_email = models.EmailField(blank=True, null=True, default=None)
    # customer_name = models.CharField(max_length=120,blank=True, null=True, default=None)
    # customer_tel = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    # # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id)
    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * self.price_per_item

        order = self.order

        all_product_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

        order_total_price = 0
        for item in all_product_in_order:
            order_total_price = order_total_price + item.total_price

        self.order.total_price =order_total_price
        self.order.save(force_update=True)
        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender,instance,created,**kwargs):
   order = instance.order
   all_product_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

   order_total_price = 0
   for item in all_product_in_order:
     order_total_price += item.total_price

   instance.order.total_price = order_total_price
   instance.order.save(force_update=True)
post_save.connect(product_in_order_post_save, sender = ProductInOrder)
# ----------------------------------END PRODUCT IN ORDRE----------------------------------------------------------

# ----------------------------------PRODUCT IN BASKET----------------------------------------------------------
class  ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128,blank=True, null=True, default=None)
    image = models.CharField(max_length=128,blank=True, null=True, default=None)
    # ссылк на заказ
    order = models.ForeignKey(Order,blank=True, null=True, default=None,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0)#price*nmb
    # customer_email = models.EmailField(blank=True, null=True, default=None)
    # customer_name = models.CharField(max_length=120,blank=True, null=True, default=None)
    # customer_tel = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    # # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id)
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * self.price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)
# ----------------------------------END PRODUCT IN ORDRE----------------------------------------------------------

#-----------------------------------subscribe---------------------------------------------------------------------
class  Subscribe(models.Model):
    email = models.EmailField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return "Подписка %s " % (self.id)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Пдписчики'
#-----------------------------------subscribe-------------------------------------------------------------


class  Wishlist(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete=models.CASCADE)

    def __str__(self):
        return "Избранное %s " % (self.id)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
