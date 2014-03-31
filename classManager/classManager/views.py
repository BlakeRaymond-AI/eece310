from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def main(request):
    return render(request, "index.html", {"first_name": request.user.first_name})
