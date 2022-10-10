from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def serviciosCapex(request):    
    return render(request, 'gcia_plan/capex/servicios/servicios.html')
