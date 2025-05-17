from django.db import models

# Create your models here.

class Servicebill(models.Model):
    servicebill_date=models.DateField(auto_now_add=True)
    servicebill_amount=models.CharField(max_length=100)
    servicebill_noofdays=models.CharField(max_length=100) 
    servicebill_details=models.CharField(max_length=200)
    servicebill_additionaldetails=models.CharField(max_length=200)
    servicebill_partamount=models.CharField(max_length=100)
    assignedservicebooking=models.ForeignKey('Admin.Assignservicebook',on_delete=models.SET_NULL,null=True)
    
     
