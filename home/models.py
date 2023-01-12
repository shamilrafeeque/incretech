from django.db import models

# Create your models here.


class Order(models.Model):
    order_date = models.DateTimeField()
    customer = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self) -> str:
        return self.customer