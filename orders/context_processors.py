from .models import ProductInBasket
from products.models import *
from .models import Wishlist
def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    # products_total_price = products_in_basket.total_price.count()
    cart_total_price = 0
    for product_in_basket in products_in_basket:
        cart_total_price += product_in_basket.total_price

    cart_nmb = 0
    for product_in_basket in products_in_basket:
        cart_nmb += product_in_basket.nmb
    


    return locals()
