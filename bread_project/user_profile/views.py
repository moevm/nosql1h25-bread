from django.shortcuts import render

# Create your views here.


def show_profile(request):
    template = "user_profile/show_profile.html"
    return render(request, template_name=template)
