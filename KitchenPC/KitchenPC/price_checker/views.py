from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def price_checker(request):
    return HttpResponse("Here are a list of prices! Enjoy! :)")

