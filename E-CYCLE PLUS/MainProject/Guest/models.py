from django.db import models

# Create your models here.



class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='UserDocs/')
    user_proof=models.FileField(upload_to='UserDocs/')
    user_password=models.CharField(max_length=50)
    user_address=models.CharField(max_length=100)
    place=models.ForeignKey('Admin.Place',on_delete=models.CASCADE)
    
class Admin(models.Model):
    admin_name=models.CharField(max_length=100,null=True)
    admin_email=models.CharField(max_length=100)
    admin_password=models.CharField(max_length=50)

    