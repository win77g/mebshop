from django.conf.urls import url,include
from django.urls import path,include
from  .views import checkout,delete_item_in_basket

urlpatterns = [
    # path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', checkout),
    # path('delete_item_in_basket/product_id/', delete_item_in_basket, name='delete_item_in_basket'),
    # path(r'^cart/$',views.cart, name='cart'),
    # path(r'^basket_top/$',views.basket_top, name='basket_top'),
    # path(r'^add_to_cart/(?P<product_id>\w+)/$',views.add_to_cart, name='add_to_cart'),
    # path(r'^add_to_cart_wishlist/(?P<product_id>\w+)/$',views.add_to_cart_wishlist, name='add_to_cart_wishlist'),
]
