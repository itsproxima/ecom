from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
from .models import *
from utils import dbconnection 
from utils import datajsonify

# Create your views here.
class resisterView(APIView):
	def get(self,request,id):
		# data=request.data
		queryset=user.objects.filter(id=id)
		serializer=UserSerializer(queryset,many=True)
		# return Response({"data":serializer.data,"status":"200 ok","message":"success"},status=200)
		return Response(serializer.data)

	def post(self,request):
		data=request.data
		email=data["email"]
		query="select * from user_user where email='"+email+"'"
		result=dbconnection.executeQuery(query)

		if(not result):
			serializer =UserSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return Response({"data":serializer.data,"status":"200","message":"u have registered successfully"},status=200)
			else:
				return Response(serializer.errors)

		else:
			return Response({"data":request.data,"status":"403","message":"u have already registered "},status=403)





		# serializer =UserSerializer(data=data)
		# if serializer.is_valid():
		# 	serializer.save()
		# 	return Response("success")
# class loginView(APIView):
	# def post(self,request,):
	# 	queryset=user.objects.filter(email=email,password=password)
	# 	serializer=UserSerializer(queryset,many=True)
	# 	# return Response({"data":serializer.data,"status":"200","message":"success"},status=200)
	# 	return Response(serializer.data)
	# 	# data=request.data
		
	# 	# serializer =UserSerializer(data=data)
	# 	# vemail=email
	# 	# vpassword= password
	# 	# queryset=user.objects.filter(email=vemail,password=vpassword)
	# 	# serializer=UserSerializer(queryset,many=True)
	# 	# return Response(serializer.data)
class userView(APIView):
	def post(self,request):
		data=request.data
		email=data["email"]
		password=data["password"]
		query="select * from user_user where email='"+email+"'"
		result=dbconnection.executeQuery(query)
		
		if(result):
			if(password==result[0]["password"]):
				# 
				request.session['user_id'] = result[0]["id"]
				#return Response("u have been logged in "+result[0]["name"])
				#json_response()
				return Response({"data":result[0],"status":"200","message":"u have been logged in"},status=200)

			else:
				return Response({"data":"","status":"403","message":"credential does not match"},status=403)
		#print(x[0][0])
		# print(result[0]["password"])
		# return Response(result)








