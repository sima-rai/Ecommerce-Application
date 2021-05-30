from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Admin, Customer, Product, Cart, Order, CartProduct, Category])
