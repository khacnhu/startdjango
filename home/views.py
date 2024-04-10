from django.shortcuts import render

# Create your views here.

def get_home(request):
    return render(request, 'home.html')