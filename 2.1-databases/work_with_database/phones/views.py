from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    tpe_srt = request.GET.get("sort", "min_price")
    phone_options = {
        'min_price': {'colloum': 'price', 'dir': -1},
        'max_price': {'colloum': 'price', 'dir': 1},
        'name': {'colloum': 'name', 'dir': 1},
    }
    phones = Phone.objects.order_by(phone_options.get(tpe_srt).get('colloum'))[::phone_options.get(tpe_srt).get('dir')]
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_slug = Phone.objects.filter(slug=slug)[0]
    template = 'product.html'
    context = {'phone': phone_slug}
    return render(request, template, context)
