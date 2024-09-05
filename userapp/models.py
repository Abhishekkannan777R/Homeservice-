from django.db import models

# Create your models here.


class regtb3(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    contact=models.IntegerField()
    date=models.DateField()
    gender=models.CharField(max_length=20)
    image=models.FileField(upload_to='pictures')     
    address=models.CharField(max_length=30)
    option=models.CharField(max_length=20)
    verified=models.BooleanField(default=False)


class servicetb3(models.Model):
    owner=models.ForeignKey(regtb3,on_delete=models.CASCADE)    
    date=models.IntegerField()
    service=models.CharField(max_length=20)
    idd=models.CharField(max_length=20)
    image=models.FileField(upload_to='pictures') 
    is_complete=models.BooleanField(default=False) 
    

class booktb3(models.Model):     
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed')
        
    ] 

  

    bname=models.CharField(max_length=20)
    usename=models.CharField(max_length=20)
    bmobile=models.IntegerField()
    baddress=models.CharField(max_length=20)
    service=models.CharField(max_length=20)
    serviceman=models.CharField(max_length=20)
    contact=models.IntegerField()
    cusername = models.CharField(max_length=20, null=True, blank=True)
    date=models.DateField()
    days =models.IntegerField()
    subamount= models.IntegerField(null=True, blank=True)
    billamount= models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

class emtb3(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    message=models.CharField(max_length=50)
    
    
    
    

   

    