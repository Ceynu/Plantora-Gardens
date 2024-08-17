from django.contrib import admin
from . models import customer
from . models import plantshop
from . models import product
from . models import cartitem
from . models import orders
from . models import newaddress

# Register your models here.
class customeradmin(admin.ModelAdmin):
    list_display = ('name','gender','contact_number','street_address','city','state','zipcode','country','email','password')

class plantshopadmin(admin.ModelAdmin):
    list_display = ('name','contact_number','street_address','city','state','zipcode','country','email','password')

class productadmin(admin.ModelAdmin):
    list_display = ('product_name','price','category','description','shop_name','image')

class cartitemadmin(admin.ModelAdmin):
    list_display = ('user','product','quantity')

class ordersadmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','ordered_date')

class newaddressadmin(admin.ModelAdmin):
    list_display = ('user','street_address','city','state','zipcode','country')


admin.site.register(customer,customeradmin)
admin.site.register(plantshop,plantshopadmin)
admin.site.register(product,productadmin)
admin.site.register(cartitem,cartitemadmin)
admin.site.register(orders,ordersadmin)
admin.site.register(newaddress,newaddressadmin)

