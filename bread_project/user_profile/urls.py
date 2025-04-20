from django.urls import path
from . import views


app_name = "user_profile"

urlpatterns = [
    path("", views.show_profile, name="show_profile"),
]
