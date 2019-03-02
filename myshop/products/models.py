from django.db import models

# Create your models here.
class categories(models.Model):
	category_name=models.CharField(max_length=100)
	image=models.CharField(max_length=500)
	is_active=models.IntegerField()

	def __str__(self):
		return "{} - {}".format(self.category_name,self.is_active)

class products(models.Model):
	name=models.CharField(max_length=100)
	desc=models.CharField(max_length=500)
	price=models.CharField(max_length=100)
	image=models.CharField(max_length=100)
	cat_id=models.ForeignKey(categories,on_delete=models.CASCADE)
	is_active=models.IntegerField()

	def __str__(self):
		return "{} - {}".format(self.name,self.desc,self.price,self.image,self.cat_id,self.is_active)