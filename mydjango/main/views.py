from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4> Hello </h4>")

def home(request):
    return HttpResponse("<h4> My home </h4>")
