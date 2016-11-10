from django.shortcuts import render, redirect

def index(request):
    return render(request, 'djanGold/index.html')

# Create your views here.
