from django.db import models
from django.utils import timezone

# Create your models here.
class customer(models.Model):
        name=models.CharField(max_length=100)
        gender = models.CharField(max_length=30)
        contact_number = models.CharField(max_length=100)
        street_address = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=100)
        zipcode = models.CharField(max_length=100)
        country = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        password = models.CharField(max_length=100)
        image = models.ImageField(upload_to='customer', null=True, blank=True)

        def __str__(self):
            return self.name
        

class plantshop(models.Model):
        name=models.CharField(max_length=100) 
        contact_number = models.CharField(max_length=100)
        street_address = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=100)
        zipcode = models.CharField(max_length=100)
        country = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        password = models.CharField(max_length=100)
        image = models.ImageField(upload_to='logo', null=True, blank=True)

        def __str__(self):
            return self.name
        
class product(models.Model):
        product_name=models.CharField(max_length=100)
        price=models.CharField(max_length=100)
        category=models.CharField(max_length=100)
        description=models.CharField(max_length=300)
        shop_name=models.ForeignKey(plantshop, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='plant')

        def __str__(self):
            return f"{self.shop_name} added product {self.product_name}"

class cartitem(models.Model):
        user = models.ForeignKey(customer,on_delete=models.CASCADE)
        product = models.ForeignKey(product,on_delete=models.CASCADE)
        quantity = models.IntegerField(default=1)

        def __str__(self):
            return f"{self.user} added {self.product} to cart"
        

class newaddress(models.Model):
        user = models.ForeignKey(cartitem,on_delete=models.CASCADE)
        street_address = models.CharField(max_length=300)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=100)
        zipcode = models.CharField(max_length=100)
        country = models.CharField(max_length=100)
        ordered_date = models.DateField(default=timezone.now)

        def __str__(self):
            return self.street_address
        
        
class orders(models.Model):
        user = models.ForeignKey(customer,on_delete=models.CASCADE)
        product = models.ForeignKey(cartitem,on_delete=models.CASCADE)
        quantity = models.CharField(max_length=100)
        ordered_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return f"{self.user} ordered {self.product}"
    