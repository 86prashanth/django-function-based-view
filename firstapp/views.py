from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse("<h2>This is first html</h2>")

def second(request):
    return render(request,'app/home.html')