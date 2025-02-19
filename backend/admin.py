from django.contrib import admin
from .models import Product, Customer, Category, Order
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','stock']
    list_filter = ['name','price']
    search_fields = ['name','description']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product','quantity','total_price','customer','order_date']
    list_display_links = ['id', 'product', 'customer']
    list_filter = ['product','order_date']
    search_fields = ['order_date','product']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
