from rest_framework import serializers
from .models import *
#from rest_framework import exception 

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=categories

		fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=products

		fields= '__all__'

