from multiprocessing import context
from django.shortcuts import render
from .models import IceCream

# Create your views here.
def get_ice_cream(request,ice_cream_id):
    icecream = IceCream.objects.get (id = ice_cream_id)
    print(icecream)
    context = {
        "icecream": {
            "id": icecream.id,
            "name": icecream.name,
            "shop": icecream.shop,
            "stock": icecream.stock

        }
    }
    return render (request,"ice_cream_detail.html",context)