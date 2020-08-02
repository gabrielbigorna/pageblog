from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    return render(request, '_links/_inicio.html')

def login(request):
    return render(request, '_links/_login.html')

def registro(request):
    return render(request, '_links/_registro.html')