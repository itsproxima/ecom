from django.db import models

# Create your models here.


class categories(models.Model):
	category_name=models.CharField(max_length=100)
	image=models.CharField(max_length=500)
	is_active=models.IntegerField()

class products(models.Model):
	name=models.CharField(max_length=100)
	desc=models.CharField(max_length=500)
	price=models.CharField(max_length=100)
	image=models.CharField(max_length=100)
	cat_id=models.ForeignKey(categories,on_delete=models.CASCADE)
	is_active=models.IntegerField()

