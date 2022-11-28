from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def recipe(request):
    return HttpResponse("Hello World. You are at the recipes index.")