from backend import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (AllProductsView, ProductView, CategoryProductView,
                    product_template, ProductListView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name ='product_list'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('',views.HomeTemplateView.as_view(), name='home'),
    path('product/<int:pk>/', product_template, name='product'),
    path('category/<int:pk>/', views.CategoryTemplateView.as_view(), name='category'),
    path('contact/',views.ContactTemplateView.as_view(), name='contact'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('products/', AllProductsView.as_view(), name ='products'),
    path('products/<int:product_id>/', ProductView.as_view(), name='product_detailed'),
    path('products/category/<int:category_id>/', CategoryProductView.as_view(), name='category_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('categories', views.CategoryListView.as_view(), name='categories'),
    path('basket', views.basket_template, name='basket'),
    path('order', views.order_template, name='order'),
]



