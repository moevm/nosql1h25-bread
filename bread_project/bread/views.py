from django.shortcuts import render
import datetime

# Create your views here.

breads = [
    {
        "title": "Белый хлеб",
        "image": "images/bread1.jpg",
        "description": "Мука, вода, дрожжи...",
        "rating": 4.3,
        "date": datetime.datetime(2024, 4, 10),
    },
    {
        "title": "Чиабатта",
        "image": "images/bread2.jpg",
        "description": "Оливковое масло, мука...",
        "rating": 3.8,
        "date": datetime.datetime(2024, 4, 15),
    },
    {
        "title": "Бублик",
        "image": "images/bread3.jpg",
        "description": "Семечки, соль, сахар...",
        "rating": 4.3,
        "date": datetime.datetime(2024, 4, 20),
    },
    {
        "title": "Ржаной хлеб",
        "image": "images/bread4.jpg",
        "description": "Ржаная мука и вода...",
        "rating": 3.5,
        "date": datetime.datetime(2024, 4, 22),
    },
    {
        "title": "Фокачча",
        "image": "images/bread5.jpg",
        "description": "Розмарин, масло...",
        "rating": 4.8,
        "date": datetime.datetime(2024, 4, 25),
    },
    {
        "title": "Батон",
        "image": "images/bread6.jpg",
        "description": "Мягкий классический хлеб",
        "rating": 3.5,
        "date": datetime.datetime(2024, 4, 30),
    },
    {
        "title": "Бриошь",
        "image": "images/bread7.jpg",
        "description": "Сладкий и маслянистый",
        "rating": 3.2,
        "date": datetime.datetime(2024, 5, 1),
    },
    {
        "title": "Лепёшка",
        "image": "images/bread8.jpg",
        "description": "Тонкий и ароматный",
        "rating": 3.8,
        "date": datetime.datetime(2024, 4, 15),
    },
]


def bread_list(request):
    template = "bread/bread_list.html"
    context = {"breads": breads}
    return render(request, template_name=template, context=context)


def bread_detail(request, pk):
    template = "bread/bread_detail.html"
    context = {"bread": breads[pk - 1]}
    return render(request, template_name=template, context=context)
