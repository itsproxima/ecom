from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from .models import *
from utils import dbconnection 

# Create your views here.
class categoryView(APIView):
        def get(self,request):
                # data=request.data
                queryset=categories.objects.all()
                serializer=CategorySerializer(queryset,many=True)
                # return Response({"data":serializer.data,"status":"200 ok","message":"success"},status=200)
                return Response(serializer.data)

        def post(self,request):
                data=request.data
                serializer =CategorySerializer(data=data)
                if serializer.is_valid():
                        serializer.save()
                        return Response("success")


class productView(APIView):
        def post(self,request):
                data=request.data
                serializer =ProductSerializer(data=data)
                if serializer.is_valid():
                        serializer.save()
                        return Response("success")
        def get(self,request):
                # data=request.data
                queryset=products.objects.all()
                serializer=ProductSerializer(queryset,many=True)
                # return Response({"data":serializer.data,"status":"200 ok","message":"success"},status=200)
                return Response(serializer.data)

class single_productView(APIView):
        def get(self,request,pid):
                data=request.data
                p_id=pid
                query="select *from products_products where id='"+str(p_id)+"'"
                result=dbconnection.executeQuery(query)
                if(result):
                        return Response({"data":result[0],"status":"200","message":"your required product"},status=200)
                else:
                        return Response({"data":"","status":"403","message":"product not found"},status=403)




class catwise_productView(APIView):
        def get(self,request,cid):
                data=request.data
                cat_id=cid
                query1="select products_products.name from products_products join products_categories on products_products.cat_id_id=products_categories.id where cat_id_id=1"
                query="select * from products_products where cat_id_id='"+str(cat_id)+"'"
                result=dbconnection.executeQuery(query)
                if(result):
                        return Response({"data":result[0],"status":"200","message":"your required product"},status=200)
                else:
                        return Response({"data":"","status":"403","message":"id does not matched "},status=403)
