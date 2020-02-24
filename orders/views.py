from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .models import ProductInBasket
from products.models import Product
from django.core import serializers
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

# Create your views here.
def basket_adding(request):

    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    image = data.get("image")
    # print(image)
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,product_id=product_id,defaults={"nmb":nmb},image=image,)
    # выбрать продукт по id
    # prod = Product.objects.filter(id=product_id)
    if not created:
        # print ("not created")
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    products_total_nmb = products_in_basket.count()
    # cart_nmb = products_in_basket.nmb.count()
     # products_total_nmb = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
    return_dict["products_total_nmb"] = products_total_nmb
    # return_dict["cart_nmb"] = cart_nmb
    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    cart_total_price = 0
    for product_in_basket in products_in_basket:
        cart_total_price += product_in_basket.total_price
    return_dict["cart_total_price"] = cart_total_price

    cart_nmb = 0
    for product_in_basket in products_in_basket:
        cart_nmb += product_in_basket.nmb
    return_dict["cart_nmb"] = cart_nmb

    # print(products_in_basket)
    # return JsonResponse(return_dict)
    return render(request, 'mod.html',locals())
    # return print('ok')

# корзина
def cart(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    cart_total_price = 0
    for product_in_basket in products_in_basket:
        cart_total_price += product_in_basket.total_price
    # передача измененной формы на вьюху
    if request.POST:
        # print (request.POST)
        if request.POST:
            # print ("yes.cart")
            data = request.POST
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    products_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_baskets = ProductInBasket.objects.get(
                        session_key=session_key,
                        is_active=True,
                        product__id = products_in_basket_id)
                    product_in_baskets.nmb = value
                    # print (value)
                    product_in_baskets.save(force_update=True)



        return HttpResponseRedirect('/cart/')
    else:
            print ("now")
    # return render(request, 'landing/cart.html', locals())
    return render(request, 'cart.html', locals())


    # для верхней корзины
    # для верхней корзины
def basket_top(request):
    return_dict = dict()
    session_key = request.session.session_key
    # print (request.POST)
    data = request.POST
    # product_id = data.get("product_id")
    # nmb = data.get("nmb")

    # new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,product_id=product_id,defaults={"nmb":nmb})
    # if not created:
    #     print ("not created")
    #     new_product.nmb += int(nmb)
    #     new_product.save(force_update=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    # cart_nmb = products_in_basket.nmb.count()
     # products_total_nmb = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
    return_dict["products_total_nmb"] = products_total_nmb
    # return_dict["cart_nmb"] = cart_nmb
    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    cart_total_price = 0
    for product_in_basket in products_in_basket:
        cart_total_price += product_in_basket.total_price
    return_dict["cart_total_price"] = cart_total_price

    cart_nmb = 0
    for product_in_basket in products_in_basket:
        cart_nmb += product_in_basket.nmb
    return_dict["cart_nmb"] = cart_nmb
    # print(return_dict)
    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False)

    total_price = 0
    for product_in_basket in products_in_basket:
        total_price += product_in_basket.total_price

    # передаем форму на вьюху
    form = CheckoutContactForm(request.POST or None)
    if request.POST:

        if form.is_valid():
            data = request.POST
            print(data)
            surnume = data["surname"]
            name = data.get("name", "serg")
            phone = data["phone"]
            mail = data["email"]
            city = data["city"]
            street = data["street"]
            text = data["text"]
            token = data["csrfmiddlewaretoken"]
            user, created = User.objects.get_or_create(username = name, defaults ={"first_name": name })

            order = Order.objects.create(user = user,
                                         customer_email = mail,
                                         customer_name = name,
                                         customer_surname = surnume,
                                         customer_tel = phone,
                                         customer_city = city,
                                         customer_street = street,
                                         comments = text,
                                         status_id = 1,
                                         token = token)

            # print(products_in_basket)
            for name in products_in_basket:
                if name:
                    products_in_basket_id = name.id
                    product_in_baskets = ProductInBasket.objects.get(session_key=session_key, is_active=True,id = products_in_basket_id )

                    product_in_baskets.save(force_update=True)
                    ProductInOrder.objects.create(
                                                 # id = order.id,
                                                 product = product_in_baskets.product,
                                                 nmb = product_in_baskets.nmb,
                                                 price_per_item = product_in_baskets.price_per_item,
                                                 total_price = product_in_baskets.total_price,
                                                 order = order,


                    )

            # products_in_basket.delete()
            # html_message = loader.render_to_string(
            # 'html_order.html',
            # {
            #
            #
            #      'phone' : data["phone"],
            #      'mail': data["email"]
            #
            # }

        # )
            products_in_basket.delete()
            # send_mail('Интернет магазин всякой х-ни',
            #                   'Ваш заказ принят,наберитесь терпения и ждите...',
            #                   'sergsergio777@gmail.com',
            #                   # 'tek-shop@mail.ru',
            #                   [mail],
            #                   # html_message=html_message,
            #                   )

            request.session['order'] = data

            # print(data)
            return HttpResponseRedirect('/order/')
        else:
            print ("now")
    return render(request,'checkout.html',locals())

def order(request):
    if request.session.has_key('order'):
        order= request.session.get('order')

        token = order["csrfmiddlewaretoken"]

        item = Order.objects.filter(token = token)
        print(item)
        d = item[0]

        productinorder = ProductInOrder.objects.filter(order = d)


    return render(request,'order.html',locals())
# --------------Create PDF File-------------------------------------

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

# --------------delete item in modal backet-----------------
def delete_item_in_basket(request,id):
    session_key = request.session.session_key
    products_in_baskets = ProductInBasket.objects.get (session_key=session_key, is_active=True,product_id = id )
    products_in_baskets.delete()
    # return render(request, 'landing/checkout.html', locals())
    return HttpResponseRedirect('/cart/')
