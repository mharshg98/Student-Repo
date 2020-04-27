from django.db import models

# Create your models here.
class Upload(models.Model):
    email=models.CharField(max_length=50)
    title=models.CharField(max_length=100,default='')
    subtitle=models.CharField(max_length=100,default='')
    Class=models.CharField(max_length=10,default='')
    stream=models.CharField(max_length=50,default='')
    subject=models.CharField(max_length=50,default='')
    url=models.CharField(max_length=300)
    date=models.DateField(default='2020-04-01')
    def __str__(self): 
         return self.title
