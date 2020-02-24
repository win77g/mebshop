"""mebshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from homepage.views import index
from django.conf.urls.static import static
from django.conf import settings
from products.views import product_detail,sort,category_filter,category_filter_sort
from orders.views import basket_adding,cart,basket_top,order,GeneratePDF,delete_item_in_basket
from contact.views import contact
from delivery.views import delivery
from underorder.views import underorder
from homepage.views import search,subscribe_footer,subscribe_index
from django.conf.urls import handler404

import debug_toolbar



admin.site.site_header = 'Админ ешопа ТАБУРЕТКИН'


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('homepage/search/',search),
    path('homepage/subscribe_footer/',subscribe_footer),
    path('homepage/index/',index),
    path('category/filter_sort/',category_filter_sort),
    path('category/filter/',category_filter),
    path('category/',include('products.urls')),

    path('orders/',include('orders.urls')),
    path('orders/basket_adding/',basket_adding),
    path('orders/basket_top/',basket_top),
    path('orders/delete_item_in_basket/<int:id>/', delete_item_in_basket),
    path('product/<str:slug>/', product_detail),
    path('product/sort/', sort),
    path('cart/', cart),
    path('contact/',contact),
    path('delivery/',delivery),
    path('underorder/',underorder),
    path('order/',order),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('order_pdf/', GeneratePDF.as_view()),
    # add toolbar----------------------------------------------------------------------------
    path('__debug__/', include(debug_toolbar.urls)),

]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'homepage.views.error_404_view'


