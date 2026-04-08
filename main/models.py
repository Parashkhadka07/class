from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=300)
    details=models.TextField()
    my_role=models.CharField(max_length=30 ) 

class Skills(models.Model):
    name=models.CharField(max_length=30)
    experience=models.DateField()