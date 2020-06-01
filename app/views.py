from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'app/login.html')

def home(request):
    return render(request, 'app/home.html')

def createaccount(request):
    return render(request, 'app/createaccount.html')
