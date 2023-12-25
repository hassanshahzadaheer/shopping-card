
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def getRouters(request):
    return JsonResponse("Welcome to Python world", safe=False)
def getHome(request):
        return JsonResponse("Python Home", safe=False)