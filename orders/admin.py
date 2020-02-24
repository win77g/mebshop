
from django.contrib import admin
from .models import *

# добавить действие в окно выполнить действие
def make_payed(modeladmin,request,queryset):
    queryset.update (status=3)
make_payed.short_description = "Пометить как оплаченные"

def make_do(modeladmin,request,queryset):
    queryset.update (status=2)
make_do.short_description = "Пометить как выполнен"

def make_new(modeladmin,request,queryset):
    queryset.update (status=4)
make_new.short_description = "Пометить как обновленный"

# class OrderAdmin(admin.ModelAdmin):


#добавление фоток внизу прдукт админки
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Order._meta.fields]
      list_display = ('id','status','total_price','customer_surname','customer_name','customer_email','customer_tel','customer_city','customer_street','comments','created')
      list_filter = ['status']
      search_fields = ["id","total_price"]
      inlines = [ProductInOrderInline]
      actions = [make_payed,make_do,make_new]

      # actions = [make_do]
class Meta:
    model = Order
# Register your models here.
admin.site.register(Order,OrderAdmin)


class StatusAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Status._meta.fields]

class Meta:
    model = Status
# Register your models here.
admin.site.register(Status,StatusAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in ProductInOrder._meta.fields]

class Meta:
    model = ProductInOrder
# Register your models here.
admin.site.register(ProductInOrder,ProductInOrderAdmin)



class ProductInBasketAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in ProductInBasket._meta.fields]

class Meta:
    model = ProductInBasket
# Register your models here.
admin.site.register(ProductInBasket,ProductInBasketAdmin)


class SubscibeAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Subscribe._meta.fields]

class Meta:
    model = Subscribe
# Register your models here.
admin.site.register(Subscribe,SubscibeAdmin)



class WishlistAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Wishlist._meta.fields]

class Meta:
    model = Wishlist
# Register your models here.
admin.site.register(Wishlist,WishlistAdmin)
