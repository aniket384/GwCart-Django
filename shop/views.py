from django.shortcuts import render
from .models import Product, Contact, Orders, OrderUpdate
from django.http import HttpResponse
from math import ceil
import json

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil(n / 4) - (n // 4)
        allProds.append([prod, range(1, nSlides), nSlides])
    params =  {'allProds': allProds}
    return render(request, "shop/index.html", params)

def about(request):
    return  render(request, 'shop/about.html')

def contact(request):
    if request.method=='POST':

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
def search(request):
    return  render(request, 'shop/search.html')

def productView(request, myid):
    products = Product.objects.filter(id=myid)
    return render(request, 'shop/productView.html', {'product': products[0]})

def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, country=country, state=state, city=city, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')