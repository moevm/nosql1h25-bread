from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.

def bread_list(request):
    template = "bread/bread_list.html"
    breads = Recipe.objects.all()
    context = {"breads": breads}
    return render(request, template_name=template, context=context)


def bread_detail(request, pk):
    template = "bread/bread_detail.html"
    bread = get_object_or_404(Recipe, pk=pk)
    context = {"bread": bread}
    return render(request, template_name=template, context=context)
