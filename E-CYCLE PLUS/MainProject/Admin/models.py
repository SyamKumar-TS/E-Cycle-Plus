from django.db import models
from User.models import Servicebook


# Create your models here.
class District(models.Model):
    district_name=models.CharField(max_length=50)

    def __str__(self):
        return self.district_name
    
class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name    
    
class Category(models.Model):
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name    
    
class Brand(models.Model):
    brand_name=models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name
    
class Technician(models.Model):
    technician_name=models.CharField(max_length=50)
    technician_gender=models.CharField(max_length=50)
    technician_contact=models.CharField(max_length=50)
    technician_email=models.CharField(max_length=50)
    technician_password=models.CharField(max_length=50)
    technician_photo=models.FileField(upload_to='TechnicianDocs/')
    technician_experience=models.CharField(max_length=100)   
    technician_address=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class Assignservicebook(models.Model):
    asb_status=models.IntegerField(default=0)
    technician=models.ForeignKey(Technician,on_delete=models.SET_NULL,null=True)  
    servicebooking=models.ForeignKey('User.Servicebook',on_delete=models.SET_NULL,null=True)   

class EwasteCollector(models.Model):
    EwasteCollector_name=models.CharField(max_length=50)
    EwasteCollector_contact=models.CharField(max_length=50)
    EwasteCollector_email=models.CharField(max_length=50)
    EwasteCollector_photo=models.FileField(upload_to='CollectorDocs/')
    EwasteCollector_proof=models.FileField(upload_to='CollectorDocs/')
    EwasteCollector_password=models.CharField(max_length=50)
    EwasteCollector_vehicleno=models.CharField(max_length=50)
    EwasteCollector_vehiclemodel=models.CharField(max_length=50)
    EwasteCollector_vehicleimg=models.FileField(upload_to='CollectorDocs/') 

class Assignewastebooking(models.Model):
    aeb_status=models.IntegerField(default=0)
    collector=models.ForeignKey(EwasteCollector,on_delete=models.SET_NULL,null=True)  
    ewastebooking=models.ForeignKey('User.Ewastebooking',on_delete=models.SET_NULL,null=True)     

class Yard(models.Model):
    yard_name=models.CharField(max_length=50)

    def __str__(self):
        return self.yard_name
        
class Type(models.Model):
    type_name=models.CharField(max_length=50)

class Product(models.Model):
    Product_name=models.CharField(max_length=50)
    product_image=models.FileField(upload_to='ProductDocs/')   
    Product_description=models.CharField(max_length=100)
    type=models.ForeignKey(Type,on_delete=models.SET_NULL,null=True)     

class Gallery(models.Model):
    gallery_image=models.FileField(upload_to='GalleryDocs/')   
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)        
        

    