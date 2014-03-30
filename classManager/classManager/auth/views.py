from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import loader, RequestContext


def register_user(request):
    state = "Please register below..."
    username = password = str()
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            user = User.objects.create_user(email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name

            state = "You have successfully registered."
        except:
            state = "Failed to register."

    return render_to_response('register.html', {'state': state, 'username': username}, context_instance=RequestContext(request))

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username})
