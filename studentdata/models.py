from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.query import prefetch_related_objects




class Address(models.Model):
    city=models.CharField(max_length=50)
    landmark=models.CharField(max_length=50)
    postal_address=models.CharField(max_length=100)
    

class Student(models.Model):
    student_name=models.CharField(max_length=100)
    standard=models.IntegerField()
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    