from django.db import models

# Create your models here.
class adtb3(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    contact=models.IntegerField()
    image=models.FileField(upload_to='pictures')     
    address=models.CharField(max_length=30)
    