from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def order(request):
    return render(request, 'dashboard/order.html')