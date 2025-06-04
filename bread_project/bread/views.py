from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.db.models import Q
from django.utils.dateparse import parse_date
from datetime import datetime

# Create your views here.

def bread_list(request):
    template = "bread/bread_list.html"
    if request.GET.get("reset"):
        # Если нажали сброс, игнорируем фильтры
        breads = Recipe.objects.all()
        context = {
            "breads": breads,
            "query": '',
            "date_from": '',
            "date_to": '',
            "rating": '0',
        }
        return render(request, template_name=template, context=context)
    query = request.GET.get('q', '')
    date_from = request.GET.get('date-from', '')
    date_to = request.GET.get('date-to', '')
    rating = request.GET.get('rating-filter', '')

    breads = Recipe.objects.all()
    if query:
        breads = breads.filter(
            Q(Title__icontains=query) | Q(Composition__icontains=query)
        )
    # Фильтрация по дате и рейтингу в Python
    if date_from:
        date_from_obj = datetime.strptime(date_from, "%Y-%m-%d")
        breads = [b for b in breads if b.Date.date() >= date_from_obj.date()]
    if date_to:
        date_to_obj = datetime.strptime(date_to, "%Y-%m-%d")
        breads = [b for b in breads if b.Date.date() <= date_to_obj.date()]
    if rating and rating.isdigit() and int(rating) > 0:
        breads = [b for b in breads if b.Rate >= float(rating)]

    context = {
        "breads": breads,
        "query": query,
        "date_from": date_from,
        "date_to": date_to,
        "rating": rating,
    }
    return render(request, template_name=template, context=context)


def bread_detail(request, pk):
    template = "bread/bread_detail.html"
    bread = get_object_or_404(Recipe, pk=pk)
    context = {"bread": bread}
    return render(request, template_name=template, context=context)
