'''
APIs
-----------------------------------------------------

'''

##################### Librerias #####################

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from apps.apis.models import *


##################### Main Script #####################
@csrf_exempt
@require_http_methods(["GET"])
def apisList(request):
    list_apis = ListApiModelo.objects.all()
    
    return render(request, 'apis/apis.html', {'list_apis': list_apis})