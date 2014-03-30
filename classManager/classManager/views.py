from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    first_name = ""
    logged_in = False
    if 'username' in request.session:
        user = User.objects.get(username=request.session['username'])
        first_name = user.first_name
        logged_in = True
    form = {
        'first_name': first_name,
        'logged_in': logged_in
    }
    return render(request, 'index.html', form)
