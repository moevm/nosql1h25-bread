from django.urls import path
from . import views


app_name = "user_profile"

urlpatterns = [
    path("", views.show_profile, name="show_profile"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path("pre_registration", views.pre_registration, name="pre_registration"),
]
