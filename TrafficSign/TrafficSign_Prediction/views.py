from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1>Traffic Sign Prediction<h1>")
    response.write("This is an application to predict traffic sign")