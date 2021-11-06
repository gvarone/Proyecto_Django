from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    diccionario = {'insert_me':'que tul'}
    return render(request,'index.html',context=diccionario)
