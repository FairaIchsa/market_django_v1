from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return HttpResponse("<h1>Hi</h1>")
