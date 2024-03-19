from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from products.models import Product, Category


def main(request):
    category = Category.objects.all()
    product = Product.objects.all()
    query_params = request.GET.get("search")
    if query_params:
        print("data", query_params)
        print("data", query_params)
        product = product.filter(title__icontains=query_params)
        print(product)

    paginator = Paginator(product, 2)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'products': page, 'category': category,
    }
    return render(request, 'main.html', context)
def cat(request, pk):
    category = Category.objects.all()
    product = Product.objects.filter(category=pk)
    query_params = request.GET.get("search")
    if query_params:
        print("data", query_params)
        print("data", query_params)
        product = product.filter(__icontains=query_params)
        print(product)

    paginator = Paginator(product, 2)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'products': page, 'category': category,
    }

    return render(request, 'main.html', context)
def product_detail(request, pk):
    category = Category.objects.all()
    product = get_object_or_404(Product, id=pk)
    context = {
        'product': product, 'category': category,
    }
    return render(request, 'product_detail.html', context)