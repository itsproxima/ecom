from django.db import models
from user.models import *
from products.models import *

# Create your models here.
class order_status(models.Model):
	status_name=models.CharField(max_length=100)


class orders(models.Model):
	order_no=models.CharField(max_length=100)
	user_id=models.ForeignKey(user,on_delete=models.CASCADE)
	shipping_address=models.CharField(max_length=500)
	total_price=models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True, blank=True)
	updated_date = models.DateTimeField(auto_now_add=True, blank=True)
	placed_date = models.DateTimeField(auto_now_add=True, blank=True)
	order_status_id=models.ForeignKey(order_status,on_delete=models.CASCADE)
	is_paid = models.CharField(default='0',max_length=200)

	def __str__(self):
		return "{}".format(self.name)


class cart(models.Model):
	order_id=models.ForeignKey(orders,on_delete=models.CASCADE)
	product_id=models.ForeignKey(products,on_delete=models.CASCADE)
	quantity=models.CharField(max_length=500)
	cart_total_price=models.CharField(max_length=500)
	order_status_id=models.ForeignKey(order_status,on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_ordered=models.CharField(default='0',max_length=10)

