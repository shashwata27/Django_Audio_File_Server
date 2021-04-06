from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Home():
    def Home_view(*args,**kwargs):
        return HttpResponse("<h1>No Home Page</h1><p> Visit LocalHost:Port/api/")
