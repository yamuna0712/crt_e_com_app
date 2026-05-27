
from django.urls import path, include
from.views import greet,get_name,user_data,user_name

urlpatterns = [
    path("message", greet),
    path('name', get_name),
    path('data',user_data),
    path('<str:name>/', user_name),

]