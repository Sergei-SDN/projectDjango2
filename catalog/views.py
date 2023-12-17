from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Product.models import Product


# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        return context


# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'SkyStore'
#     }
#     return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        return context


# def product_detail(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'SkyStore {product_item.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)
