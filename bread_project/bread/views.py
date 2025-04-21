from re import template
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def bread_list(request):
    template = "bread_list.html"
    return render(request, template_name=template)


def bread_detail(request, pk):
    template = "bread/bread_detail.html"
    return render(request, template_name=template)
