from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import UserProfileForm


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.first_name = profile_form.cleaned_data['first_name']
            user.last_name = profile_form.cleaned_data['last_name']
            user.email = profile_form.cleaned_data['email']
            user.save()
            return HttpResponseRedirect('/')
    user_form = UserCreationForm()
    profile_form = UserProfileForm()
    return render(request, "register.html", {"user_form": user_form, "profile_form": profile_form})

@login_required
def profile(request):
    return HttpResponse("Welcome, %s!" % request.user.first_name)
