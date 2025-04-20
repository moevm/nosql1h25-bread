from . import views
from django.urls import path

app_name = "bread"

urlpatterns = [
    path("<int:pk>/", views.bread_detail, name="bread_detail"),
]
