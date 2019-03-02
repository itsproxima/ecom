from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import *
from utils import dbconnection 
import datetime

# Create your views here.
def get_product_price(product_id):
        query="SELECT price from `products_products` WHERE id='"+product_id+"'"
        result=dbconnection.executeQuery(query)
        return result

class cartView(APIView):
        def post(self,request):
                cart_data=request.data
                products_data=cart_data["products_details"]
                user_id=cart_data["uid"]
                # quantity=products_data["quantity"]
                

                def assign_order_no():
                        import random
                        number=random.randint(1,10001)
                        return number
                def get_order_details(user_id):
                        query="select * from orders_orders where user_id_id='"+user_id+"'"
                        result=dbconnection.executeQuery(query)
                        return result
                def get_product_price(product_id):
                        query="SELECT price from `products_products` WHERE id='"+product_id+"'"
                        result=dbconnection.executeQuery(query)
                        return result

                order_no=assign_order_no()
                order_details=get_order_details(user_id)
                
                if not order_details:
                        order_status_id=1
                        query="INSERT INTO `orders_orders`(`order_no`,`order_status_id_id`, `user_id_id`) VALUES ({},{},{})".format(order_no,order_status_id,user_id)
                        order_data=dbconnection.execute(query)
                        # return Response("NEW ORDER CREATED ")
                        # create the cart 
                        for product in products_data:
                                product_id=product["product_id"]
                                quantity = product["quantity"]
                                price_per_product=get_product_price(product_id)[0]["price"]
                                total_price=int(price_per_product)*int(quantity)
                                query1="INSERT INTO `orders_cart`(`quantity`, `cart_total_price`,`order_id_id`, `order_status_id_id`, `product_id_id`,`is_ordered`) VALUES ({},{},{},{},{},{})".format(quantity,total_price,order_data,order_status_id,product_id,0)
                                result=dbconnection.execute(query1)
                                # return Response("NEW ORDER CREATED ")
                        return Response("NEW ORDER CREATED ")

                else:
                        order_id=order_details[0]["id"]
                        #loop through cart
                        for product in products_data:
                                product_id=product["product_id"]
                                cart_has_data=dbconnection.execute("SELECT `id`,`quantity`,`order_id_id` FROM `orders_cart` WHERE `product_id_id`={} AND `order_status_id_id`=1 AND order_id_id= {} AND `is_ordered`=0".format(product_id,order_id))
                                if cart_has_data:
                                        quantity_per_product = cart_has_data[0]["quantity"]
                                        cart_id = cart_has_data[0]["id"]
                                        order_id = cart_has_data[0]["order_id_id"]
                                        price=get_product_price(product_id)[0]["price"]
                                        updated_quantity = int(quantity_per_product) + int(product["quantity"])
                                        total_price=updated_quantity*int(price)
                                        query="UPDATE `orders_cart` SET `quantity`={},`cart_total_price`={} WHERE `id`={}".format(updated_quantity, total_price,cart_id)
                                        update_cart=dbconnection.execute(query)
                                else:
                                        product_id =product["product_id"]
                                        quantity = product["quantity"]
                                        price=get_product_price(product_id)[0]["price"]
                                        total_price=int(price)*int(quantity)
                                        query="INSERT INTO `orders_cart`(`quantity`, `cart_total_price`,`order_id_id`, `order_status_id_id`, `product_id_id`,`is_ordered`) VALUES ({},{},{},{},{},{})".format(quantity,total_price,order_id,1,product_id,0)
                                        result=dbconnection.execute(query)
                        return Response("cart data")

class cartupdateView(APIView):
        def post(self,request):
                cart_data=request.data
                product_id = cart_data["cart"]["product_id"]
                cart_id = cart_data["cart"]["cart_id"]
                user_id = cart_data["user_id"]
                product_price=get_product_price(product_id)[0]["price"]
                new_quantity=cart_data["cart"]["quantity"]
                updated_price=int(product_price)*int(new_quantity)

                query="UPDATE `orders_cart` SET `quantity`={},`cart_total_price`={} WHERE `id`={}".format(new_quantity,updated_price,cart_id)
                result=dbconnection.execute(query)
                
                return Response("cart updated")
class cartdeleteView(APIView):
        def post(self,request):
                cart_data=request.data
                product_id = cart_data["cart"]["product_id"]
                cart_id = cart_data["cart"]["cart_id"]
                user_id = cart_data["user_id"]

                delete_cart = dbconnection.execute("DELETE FROM `orders_cart` WHERE `id`= {}".format(cart_id))

                return Response("deleted")
# class showcartView(APIView):
#     def post(self, request):

#         cart_data = request.data
#         user_id = cart_data["user_id"]

#         cart_data= dbcon.execute("SELECT orders_cart.`id`,orders_cart.`quantity`,orders_cart.`ammount`,`product_id`,products_product.price,products_product.product_name,products_product.image FROM `orders_cart` INNER JOIN products_product ON products_product.id=orders_cart.product_id WHERE `order_id` IN (SELECT id FROM orders_order WHERE orders_order.user_id={} AND orders_order.order_status_id={})".format(user_id,'1'))
       
#         response_data ={"cart_data":cart_data}
        
#         return Response({"data":response_data,"status":"00","message":"Success"}, status=200)



