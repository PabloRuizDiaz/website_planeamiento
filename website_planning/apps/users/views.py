from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import *


@csrf_exempt
@require_http_methods(["GET","POST"])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/loggeo.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'main/inicio.html')
        else:
            # Return an 'invalid login' error message.
            pass


@require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    return render(request, 'main/inicio.html')
