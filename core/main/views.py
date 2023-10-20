from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>check work</h4>')

def about(request):
    return HttpResponse('<h4>this page about us</h4>')
    