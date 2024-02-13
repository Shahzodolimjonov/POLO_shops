
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def home(requests):
    ctg = Category.objects.all()
    smeaker = Smeakers.objects.all()
    ctx = {
        'ctg': ctg,
        'smeaker': smeaker,
    }
    return render(requests, 'blog/index.html', ctx)


def contact(requests):
    ctg = Category.objects.all()
    form = ContactForm()
    if requests.POST:
        form = ContactForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    ctx = {'ctg': ctg}
    return render(requests, 'blog/contact.html', ctx)


def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    smeaker = Smeakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'smeaker': smeaker
    }
    return render(requests, 'blog/products.html', ctx)


def register(requests):
    ctg = Category.objects.all()
    form = RegisterForm()
    if requests.POST:
        form = RegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    ctx = {'ctg': ctg}
    return render(requests, 'blog/register.html', ctx)


def single(requests, pk=None):
    ctg = Category.objects.all()
    products_pk = Smeakers.objects.get(pk=pk)
    form = ChoiceForm()
    if requests.POST:
        forms = ChoiceForm(requests.POST or None,
                           requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg': ctg,
        'products_pk': products_pk,
        'form': form,
    }
    ctx = {}
    return render(requests, 'blog/single.html', ctx)


