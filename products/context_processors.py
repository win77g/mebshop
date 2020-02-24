from products.models import *

def getting_category(request):
    category = Category.objects.all()
    return locals()
