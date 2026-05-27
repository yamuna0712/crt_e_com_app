from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
#  http://127.0.0.1:4141/user/message
def greet(request):
    return HttpResponse("Hii, Good Morning")
def get_name(request):
    return HttpResponse("Hello")

def user_data(request):
    a=[
        {
            "name":"elsa",
            "email":"elsa@gmail.com",
            "address":"hyd"
        },
        {
            "name":"john",
            "email":"john@gmail.com",
            "address":"tnl"
        }
    ]
    return JsonResponse(a,safe=False)
def user_name(request, name):
    return HttpResponse(f"Hello {name}")