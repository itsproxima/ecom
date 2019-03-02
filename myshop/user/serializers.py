from rest_framework import serializers
from .models import *
#from rest_framework import exception 

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=user

		fields= '__all__'