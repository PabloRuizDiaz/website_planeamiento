from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from datetime import datetime
from apps.gcia_plan.capex.dailyCapex.models import *
from pathlib import Path
import os
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def user_check(user):
    return user.username.startswith(('admin','capex'))


@login_required(login_url='logInUser')
@user_passes_test(user_check,login_url='logInUser')
@csrf_exempt
@require_http_methods(["GET"])
def daily(request):
    return render(request, 'gcia_plan/capex/daily/daily.html')


#################### Tasas de Cambio Nuevas ####################

@csrf_exempt
@require_http_methods(["GET","POST"])
def tasaCambio(request):
    if request.method == 'GET':
        year = datetime.today().year
        list_tasa = tasasCambioModel.objects.all().filter(fecha__contains=str(year))

        return render(request, 'gcia_plan/capex/daily/tasacambio.html', {'list_tasa': list_tasa})
    
    if request.method == 'POST':
        data = tasasCambioModel(
            fecha = datetime.strptime(request.POST.get('fecha'), '%Y-%m-%d'),
            pais = (str(request.POST.get('pais'))),
            tc_plan = request.POST.get('tc_plan'),
            tc_revision = request.POST.get('tc_revision'),
            tc_proyectada = request.POST.get('tc_proyectada'))
        
        data.save()

        return redirect(tasaCambio)


#################### Actualizacion de PosPre ####################

@csrf_exempt
@require_http_methods(["GET","POST"])
def pospre(request):
    if request.method == 'GET':
        return render(request, 'gcia_plan/capex/daily/pospre.html')

    if request.method == 'POST':
        myfile = request.FILES['file']
        filename = myfile.name
        
        doc = pospreFileModel(DOC_POSPRE=myfile)
        doc.save()
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        pathfile = '{0}/../../../media/gcia_plan/capex/files/{1}' .format(BASE_DIR,filename)
        data=[]
        
        pospreModel.objects.all().delete()

        data = pd.read_excel(pathfile,header=0,keep_default_na=False).to_dict(orient='records')

        for item in data:
            object, created=pospreModel.objects.get_or_create(**item)

        os.remove(pathfile)

        return render(request, 'gcia_plan/capex/daily/okfile.html')


#################### Nuevos Proveedores ####################

@csrf_exempt
@require_http_methods(["GET","POST"])
def proveedores(request):
    if request.method == 'GET':
        list_proveedores = proveedorModel.objects.all()

        return render(request, 'gcia_plan/capex/daily/proveedores.html', {'list_proveedores':list_proveedores})

    if request.method == 'POST':
        data = proveedorModel(
            NROPROVEEDOR = (request.POST.get('NROPROVEEDOR')),
            PROVEEDOR = request.POST.get('PROVEEDOR'),
            COMEX = int(request.POST.get('COMEX')))
        
        data.save()

        return redirect(proveedores)


#################### Carga de Carry Over ####################

@csrf_exempt
@require_http_methods(["GET","POST"])
def carryOver(request):
    if request.method == 'GET':
        return render(request, 'gcia_plan/capex/daily/carryover.html')

    if request.method == 'POST':
        myfile = request.FILES['file']
        filename = myfile.name
        
        doc = pryCarryOverFileModel(DOC_PRY_CO=myfile)
        doc.save()
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        pathfile = '{0}/../../../media/gcia_plan/capex/files/{1}' .format(BASE_DIR,filename)
        
        pryCarryOverModel.objects.all().delete()

        data = pd.read_excel(pathfile,header=0,keep_default_na=False).to_dict(orient='records')
        
        for item in data:
            object, created=pryCarryOverModel.objects.get_or_create(**item)

        os.remove(pathfile)

        return render(request, 'gcia_plan/capex/daily/okfile_CO.html')