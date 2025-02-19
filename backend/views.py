from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views import generic
from .forms import ProductForm, RegistrationForm, OrderForm
from .models import *


class AllProductsView(View):
    def get(self, request):
        ask = request.GET
        products = Product.objects.all()
        if ask.get('search'):
            products = products.filter(
                Q(name__icontains= ask['search']) | Q(description__icontains=ask['search'])
            )
        filter = ask.get('filter')
        if filter:
            if filter == 'above_100':
                products = products.filter(price__gte=100)
            elif filter == 'below_100':
                products = products.filter(price__lte=100)
        print(products.query)
        list = [
            {
                'name': product.name,
                'description': product.description,
                'price': product.price
            }for product in products
        ]
        return JsonResponse(data={'list':list})

class ProductView(View):
    def get(self, request, product_id):
        product = Product.objects.filter(id = product_id).first()
        if not product:
            return JsonResponse(data={})
        product_dict = {
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'stock': product.stock
        }
        return JsonResponse(data= product_dict)


class CategoryProductView(View):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id).all()
        response = [
            {
                'name': product.name,
                'description': product.description,
                'price': product.price
            } for product in products
        ]
        return JsonResponse(data={'response': response})

def product_template(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, template_name ='product.html', context={'product' : product })

class CategoryTemplateView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            raise Exception('Form is not valid')
    else:
        form = ProductForm()
    return render(request, template_name= 'add_product.html', context= {'form':form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(to='product', pk=product.pk)
        else:
            raise Exception('Form is not valid')
    else:
        form = ProductForm(instance=product)
    return render(request, template_name= 'edit_product.html', context= {'form':form})


@login_required
def profile(request):
    return render(request, template_name= 'profile.html', context= {'user':request.user})


class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('profile')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, template_name= 'register.html',context= {'form':form})


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    queryset = Product.objects.all()
    template_name = 'product_list.html'

class ProductDetailView(generic.DetailView):
    model = Product
    def product_detail_view(request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            raise Exception('Product not exist')

        return render(
            request,
            'product_detail.html',
            context={'product': product }
        )

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'categories.html'

    def get_queryset(self):
        return Category.objects.filter().all()

    def category_detail_view(request, pk):
        try:
            category_id = Category.objects.get(pk=pk)
        except:
            raise Exception('Product not exist')

        return render(
            request,
            'categories.html',
            context={'category': category_id}
        )

def order_template(request):
    order = Order.objects.filter().all()
    return render(request, template_name ='order.html', context={'order' : order })

def basket_template(request):
    queryset = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            raise Exception('Form is not valid')
    else:
        form = OrderForm()
    return render(request, template_name= 'basket.html', context= {'form':form})




