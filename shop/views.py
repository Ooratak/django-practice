from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ContactForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'shop/contact.html', {'form': form})

def success(request):
    return render(request, 'shop/success.html')

