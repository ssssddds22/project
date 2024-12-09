from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page.html")

def page1(request):
    return render(request, "main./page1.html")

# Create your views here.
