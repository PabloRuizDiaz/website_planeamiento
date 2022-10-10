from django.shortcuts import render
from apps.gcia_plan.red.dailyRed.models import *
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from pathlib import Path
import pandas as pd
import os


def user_check(user):
	return user.username.startswith(('admin'))


@login_required(login_url='logInUser')
@user_passes_test(user_check,login_url='logInUser')
@csrf_exempt
@require_http_methods(["GET", "POST"])
def daily(request):
	if request.method == 'GET':
		return render(request, 'gcia_plan/red/daily/daily.html')


# #################### Generador de UTs ####################

# # Variables globales para trabajar en el server
# DEV = False  # Para poner en modo Dev asignar True a la Variable DEV, en este modo los datos no se guardan en la base
# ut_list = []

# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def altaUT(request):
# 	if request.method == 'GET':
# 		ut_list.clear()

# 		return render(request, 'gcia_plan/red/daily/alta_ut.html')
	
# 	if request.method == 'POST':
# 		coordenadas = request.POST.get("latlong")
# 		nombre = request.POST.get("nombre")
# 		cell_id = request.POST.get("cell")
# 		tipo_ut = request.POST.get("select",'IM')
# 		sol_esp = request.POST.get("solEspselect")
# 		direccion = request.POST.get("address")

# 		user = 'Web'
		
# 		ut_list.append(solicitar_ut(coordenadas,nombre,cell_id,tipo_ut,sol_esp,direccion,user))

# 		return render(request,'gcia_plan/red/daily/alta_ut.html', {"ut_list":ut_list})


# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def altaMasivaUT(request):
# 	if request.method == 'GET':

# 		return render(request, 'gcia_plan/red/daily/altaUtMasiva.html')
	
# 	if request.method == 'POST':
# 		myfile = request.FILES['file']
# 		filename = myfile.name
		
# 		doc = utFileModel(DOC_UT=myfile)
# 		doc.save()
		
# 		BASE_DIR = Path(__file__).resolve().parent.parent
# 		pathfile = '{0}/../../../media/gcia_plan/red/files/{1}' .format(BASE_DIR,filename)

# 		data = pd.read_excel(pathfile,header=0).fillna('').to_dict(orient='records')

# 		user = 'Web'
# 		utMasivo = []

# 		for i in data:
			
# 			utMasivo.append(solicitar_ut('{},{}' .format(i['LATITUD'], i['LONGITUD']),i['NOMBRE'],i['CELL_ID'],i['TIPO_UT'],i['SOL_ESP'],i['DIRECCION'],user))
		
# 		os.remove(pathfile)

# 		return render(request,'gcia_plan/red/daily/altaUtMasiva.html', {"utMasivo":utMasivo, 'result':1})


# def solicitar_ut(coordenadas, nombre, cell_id, tipo, sol_esp, direccion, user_creador):
# 	sap = None
	
# 	(param_latitud, param_longitud) = coordenadas.split(',')

# 	if cell_id.strip() == '':
# 		cell_id = None

# 	row = getUT(lat=param_latitud, long=param_longitud, nombre=nombre, cell_id=cell_id, tipo_ut=tipo, sol_esp= sol_esp)

# 	# Lanzar mensaje cuando no se encuentre localidad dentro de los 75 km getUT va a retornar un dic con  
# 	# {LOC_NOT_FOUND:1} \TODO Pablo Ruiz Dias
# 	if "LOC_NOT_FOUND" in row:
# 		print("###########    No se encontro localidad   ###############")
		  
# 	if row is not None:
# 		sap = Sap_BI(row['UT'],
# 					row['TIPO'],
# 					row['INDICADOR_ESTRUCTURA'],
# 					row['DENOMINACION'],
# 					row['GRUPO_DE_AUTORIZACION'],
# 					row['ID_CENTRO_EMPLAZAMIENTO'],
# 					row['ID_EMPLAZAMIENTO'],
# 					row['COD_CECO'],
# 					row['SOCIEDAD'],
# 					row['LOC_NOMBRE'],
# 					row['DPTO_NOMBRE'],
# 					row['PRV_NOMBRE'],
# 					row['LATITUD'],
# 					row['LONGITUD'],
# 					row['ALM'])
 
# 		cell_id = sap.cell_id

# 		try:
# 			cell = cellIdModel.objects.get(cell_id=cell_id[:7].upper())
		
# 		except cellIdModel.DoesNotExist:
# 			cell = cellIdModel(cell_id=cell_id[:7].upper())
			
# 		#Se actualizan los datos de la celda
# 		if cell.denominacion.strip() == '':
# 			#si no tiene un nombre previo se le pone el nombre pasado por parametro
# 			cell.denominacion = sap.denominacion
# 		else:
# 			# si ya tiene Nombre asignado se deja el nombre de la celda que tenia
# 			cell.denominacion=sap.denominacion
		
# 		cell.latitud = sap.lat
# 		cell.longitud = sap.long
# 		cell.direccion = direccion
# 		cell.localidad = sap.localidad
# 		cell.departamento = sap.departamento
# 		cell.provincia = sap.provincia
# 		cell.pais = sap.pais
# 		cell.alm = sap.alm
# 		cell.dispo = False
	
# 		if not DEV: 
# 			cell.save()
			
# 			ut = utModel(ut=sap.ut, tipo_ut=sap.tipo_ut, denominacion=sap.denominacion, cell_id=cell, creador=user_creador)
# 			ut.save()

# 	return sap