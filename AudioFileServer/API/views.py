from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Home():
    def Home_view(*args,**kwargs):
        return HttpResponse("<h1>No Home Page</h1><br><p> Visit LocalHost:Port/api/</p><br><p> Or if Admin visit LocalHost:Port/admin/</p>")
