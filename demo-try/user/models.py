from django.db import models

# Create your models here.
class user(models.Model):
	# uid= models.IntegerField()
	name=models.CharField(max_length=100)
	email= models.EmailField(max_length=100)
	password= models.CharField(max_length=100)
	phone= models.CharField(max_length=100)

class shipping_address(models.Model):
	address= models.CharField(max_length=500)
	pin=models.CharField(max_length=10)
	state=models.CharField(max_length=100)
	uid=models.ForeignKey(user,on_delete=models.CASCADE)


# class order_status(models.Model):
# 	status_name=models.CharField(max_length=500)

# class order(models.Model):
# 	order_no=models.CharField(max_length=100)
# 	date=models.CharField(max_length=100)
# 	uid=models.ForeignKey(user,on_delete=models.CASCADE)
# 	shipping_add=models.CharField(max_length=500)
# 	total_price=models.CharField(max_length=100)
# 	order_status_id=models.ForeignKey(order_status,on_delete=models.CASCADE)

# class cart(models.Model):
# 	order_id=models.ForeignKey(order,on_delete=models.CASCADE)
# 	product_id=models.ForeignKey(product,on_delete=models.CASCADE)
# 	quantity=models.CharField(max_length=100)
# 	total_price=models.CharField(max_length=100)
# 	order_status_id=models.ForeignKey(order_status,on_delete=models.CASCADE)

