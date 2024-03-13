from django.db import models

# Create your models here.
class emp (models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.CharField(max_length=50)
    phone=models.CharField( max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)