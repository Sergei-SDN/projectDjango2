from django.shortcuts import render

from Product.models import Product


# Create your views here.

def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'SkyStore'
    }
    return render(request, 'main/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contacts.html', context)


def product_detail(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'SkyStore {product_item.name}'
    }
    return render(request, 'main/product_detail.html', context)
