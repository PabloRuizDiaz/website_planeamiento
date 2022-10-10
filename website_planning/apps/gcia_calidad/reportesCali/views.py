from django.shortcuts import render
from apps.gcia_calidad.reportesCali.models import *
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests


session = requests.Session()
session.trust_env = False


@csrf_exempt
@require_http_methods(["GET"])
def reportes(request):
    dash = reporteCalidadModel.objects.filter(publicar=True).order_by('-id')

    return render(request, 'gcia_calidad/reportes.html', {"dash": dash})


@csrf_exempt
@require_http_methods(["GET"])
def cargaReporte(request, id_rep):
    if request.method == 'GET':
        reporte = reporteCalidadModel.objects.get(id=id_rep)
        reporte.visitas = reporte.visitas + 1
        reporte.save()

        if reporte.tipo == 'PBI':
            return redirect(reporte.url_pwbi)

        # Documentacion para utilizar Tableau en una website:
        # https://help.tableau.com/current/server/es-es/trusted_auth.htm
        # https://help.tableau.com/current/server/es-es/trusted_auth_webrequ.htm
        arg = {'username': reporte.user_auth, 'target_site': reporte.site}
        url = "http://tableauit02apw.ctimovil.net/trusted"
        
        response = session.post(url, data=arg, verify=False)
        
        if (response.status_code == 200 and response.text != '-1'): 
            return redirect("http://tableauit02apw.ctimovil.net/trusted/{}/t/{}/views/{}".format(response.text, reporte.site, reporte.view_id))

        # Si no responde con el vale el server de tableau, te deriva pero debes loguearte con un usuario
        return redirect('http://tableauit02apw.ctimovil.net/#/site/{}/views/{}'.format(reporte.site, reporte.view_id))
