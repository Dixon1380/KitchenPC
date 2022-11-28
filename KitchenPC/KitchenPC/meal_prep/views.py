from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def meal_prep(request):
    return HttpResponse("Here is your meal prep!")