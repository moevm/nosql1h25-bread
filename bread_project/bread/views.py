from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def bread_detail(request, pk):
    return HttpResponse(f"Хлеб номер {pk}")
