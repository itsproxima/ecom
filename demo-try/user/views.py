from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@csrf_exempt
def index(request):
	json_data = json.loads(request.body.decode("utf-8"))
	print(json_data)
	
	


	
