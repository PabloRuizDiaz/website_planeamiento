from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def user_check(user):
    return user.username.startswith(('admin','materiales'))


@login_required(login_url='logInUser')
@user_passes_test(user_check,login_url='logInUser')
@csrf_exempt
@require_http_methods(["GET"])
def dailyMat(request):    
    return render(request, 'gcia_plan/materiales/daily/daily.html')
