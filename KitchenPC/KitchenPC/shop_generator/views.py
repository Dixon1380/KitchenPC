from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def shop_generator(request):
    return HttpResponse("Shopping List is here!")