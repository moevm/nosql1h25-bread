from . import views
from django.urls import path

app_name = "bread"

urlpatterns = [
    path("", views.bread_list, name="bread_list"),
    path("<int:pk>/", views.bread_detail, name="bread_detail"),
]
