from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('THIS IS APP 1 - ONE')

def index1(request):
    return HttpResponse("RENDER THE APP INDEX 1 NHA")
