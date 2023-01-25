from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def my_view(request):
    data = {"message": "your view"}
    return JsonResponse(data)
