from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('customer', 'total_amount', 'order_date')
   


admin.site.register(Order,OrderAdmin)