from django.db import models

# Create your models here.
class Users(models.Model):
	# uid= models.IntegerField()
	uname=models.CharField(max_length=100)
	email= models.EmailField(max_length=100)
	password= models.CharField(max_length=100)
	phone= models.CharField(max_length=100)