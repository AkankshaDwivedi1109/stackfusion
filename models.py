import datetime
from django.db import models
class student(models.Model):        #models is module and Model is used for database
    Name=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    email = models.EmailField(default='example@example.com')
    d_o_b = models.DateField(default=datetime.date.today)
# Create your models here.
