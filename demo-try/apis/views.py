from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.http import JsonResponse


# Create your views here.
# def index(request):
# 	return HttpResponse("<h1>this is working</h1>")
def index(request):
	all_users= Users.objects.all()
	html= ''
	for user in all_users:
		html+=user.uname

	data = {"results": list(all_users.values("id", "uname", "email"))}
	# return HttpResponse(html)
	return JsonResponse(data)
		
