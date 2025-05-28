from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.db.models import Q

# Create your views here.

def bread_list(request):
    template = "bread/bread_list.html"
    query = request.GET.get('q', '')
    if query:
        breads = Recipe.objects.filter(
            Q(Title__icontains=query) | Q(Composition__icontains=query)
        )
    else:
        breads = Recipe.objects.all()
    context = {"breads": breads, "query": query}
    return render(request, template_name=template, context=context)


def bread_detail(request, pk):
    template = "bread/bread_detail.html"
    bread = get_object_or_404(Recipe, pk=pk)
    context = {"bread": bread}
    return render(request, template_name=template, context=context)
