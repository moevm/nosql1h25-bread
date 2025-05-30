from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserEditForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("bread:bread_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/registration_form.html", {"form": form})


@login_required
def show_profile(request):
    template = "user_profile/show_profile.html"
    return render(request, template_name=template)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user_profile:show_profile")  # Редирект на страницу профиля
    else:
        form = CustomUserEditForm(instance=request.user)

    return render(request, "user_profile/edit_profile.html", {"form": form})


def pre_registration(request):
    template = "user_profile/pre_registration.html"
    return render(request, template_name=template)
