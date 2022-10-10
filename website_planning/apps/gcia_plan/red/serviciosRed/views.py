##################### Librerias #####################
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from apps.gcia_plan.red.serviciosRed.models import *
# import cx_Oracle
# from apps.basedata.config import config
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import unidecode
# from pathlib import Path
# import os
# import pandas as pd
from apps.gcia_plan.red.dailyRed.models import *


@csrf_exempt
@require_http_methods(["GET"])
def serviciosRed(request):    
	return render(request, 'gcia_plan/red/servicios/servicios.html')


##################### Proyectos Core #####################
@csrf_exempt
@require_http_methods(["GET","POST"])
def main_proyecto_core(request):
	list_all_pry = ListPryModelo.objects.all().values('ID', 'PROYECTO_GCIA', 'GERENCIA')
	list_pry_act = ListPryModelo.objects.filter(ESTADO='activo').values('ID', 'PROYECTO_GCIA', 'GERENCIA')
	list_model_pry = ListPryModelo.objects.all()
	list_model_status = SeguiPryModelo.objects.select_related().all()
	
	return render(request, 'gcia_plan/red/servicios/prycore.html', 
			{'list_all_pry': list_all_pry, 'list_pry_act': list_pry_act, 
			'list_model_pry': list_model_pry, 'list_model_status': list_model_status})


@csrf_exempt
@require_http_methods(["POST"])
def nuevo_proyecto_core(request):
	if request.method == 'POST':
		fecha_creacion = datetime.today()

		fecha_inicio_est = datetime.strptime(
			request.POST.get('fecha_inicio_estimada'), '%Y-%m-%d')
		fecha_fin_est = datetime.strptime(
			request.POST.get('fecha_fin_estimada'), '%Y-%m-%d')

		try:
			data = ListPryModelo(
				PROYECTO_SAP=(str(request.POST.get('proyecto_sap'))),
				CEGE_UNIVERSAL=(str(request.POST.get('cege_universal'))),
				PROYECTO_GCIA=(str(request.POST.get('proyecto_gcia'))),
				USUARIO_REPORTE=(str(request.POST.get('legajo')).upper()),
				ESTADO=(str(request.POST.get('estado'))),
				ALCANCE=(str(request.POST.get('alcance'))),
				ANIO_SAP=(str(request.POST.get('anio_sap'))),
				PAIS=(str(request.POST.get('pais'))),
				RED=(str(request.POST.get('red'))),
				VALORACION=(str(request.POST.get('valoracion'))),
				RESPONSABLE=(str(request.POST.get('responsable'))),
				GERENCIA=(str(request.POST.get('gerencia'))),
				FECHA_INICIO_ESTIMADA=fecha_inicio_est,
				FECHA_FIN_ESTIMADA=fecha_fin_est,
				FECHA_CREACION=fecha_creacion)

			data.save()

			list_all_pry = ListPryModelo.objects.all().values('ID', 'PROYECTO_GCIA', 'GERENCIA')
			list_pry_act = ListPryModelo.objects.filter(ESTADO='activo').values('ID', 'PROYECTO_GCIA', 'GERENCIA')
			list_model_pry = ListPryModelo.objects.all()
			list_model_status = SeguiPryModelo.objects.select_related().all()

			return render(request, 'gcia_plan/red/servicios/prycore.html',
				{'list_all_pry': list_all_pry, 'list_pry_act': list_pry_act, 
				'list_model_pry': list_model_pry, 'list_model_status': list_model_status})

		except:
			return HttpResponse('<H1>ERROR</H1>')


@csrf_exempt
@require_http_methods(["POST"])
def actualizar_proyecto_core(request):
	if request.method == 'POST':
		try:
			data_pry = ListPryModelo(
				ESTADO=(str(request.POST.get('estado'))),
				USUARIO_REPORTE=(str(request.POST.get('legajo')).upper()),
				FECHA_INICIO_REAL=datetime.strptime(
					request.POST.get('fecha_inicio_real'), '%Y-%m-%d'),
				FECHA_FIN_REAL=(datetime.strptime((request.POST.get('fecha_fin_real') if request.POST.get(
					'fecha_fin_real') != '' else '9999-12-31'), '%Y-%m-%d')),
				FECHA_CANCELACION=datetime.strptime((request.POST.get('fecha_cancelacion') if request.POST.get(
					'fecha_cancelacion') != '' else '9999-12-31'), '%Y-%m-%d'),
				MOTIVO_CANCELACION=(str(request.POST.get('motivo_cancelacion'))))

			ListPryModelo.objects.filter(ID=str(request.POST.get('proyecto_id'))).update(
				ESTADO=data_pry.ESTADO,
				USUARIO_REPORTE=data_pry.USUARIO_REPORTE,
				FECHA_INICIO_REAL=data_pry.FECHA_INICIO_REAL,
				FECHA_FIN_REAL=data_pry.FECHA_FIN_REAL,
				FECHA_CANCELACION=data_pry.FECHA_CANCELACION,
				MOTIVO_CANCELACION=data_pry.MOTIVO_CANCELACION)
			
			list_all_pry = ListPryModelo.objects.all().values('ID', 'PROYECTO_GCIA', 'GERENCIA')
			list_pry_act = ListPryModelo.objects.filter(ESTADO='activo').values('ID', 'PROYECTO_GCIA', 'GERENCIA')
			list_model_pry = ListPryModelo.objects.all()
			list_model_status = SeguiPryModelo.objects.select_related().all()

			return render(request, 'gcia_plan/red/servicios/prycore.html',
				{'list_all_pry': list_all_pry, 'list_pry_act': list_pry_act, 
				'list_model_pry': list_model_pry, 'list_model_status': list_model_status})

		except:
			return HttpResponse('<H1>ERROR</H1>')


@csrf_exempt
@require_http_methods(["POST"])
def actualizar_estado_proyecto_core(request):
	if request.method == 'POST':
		try:
			data_act_pry = SeguiPryModelo(
				PROYECTO_ID=ListPryModelo(
					int(request.POST.get('proyecto_gcia'))),
				USUARIO_REPORTE=(str(request.POST.get('legajo')).upper()),
				FECHA_REPORTE=datetime.today(),
				FASE_COMPRAS=(str(request.POST.get('fase_compras'))),
				FASE_PREPARACION=(str(request.POST.get('fase_preparacion'))),
				FASE_IMPLEMENTACION=(
					str(request.POST.get('fase_implementacion'))),
				FASE_PRUEBAS=(str(request.POST.get('fase_pruebas'))),
				FASE_PRODUCCION=(str(request.POST.get('fase_produccion'))),
				SITUACION=(str(request.POST.get('situacion'))),
				FECHA_REPLAN=datetime.strptime((request.POST.get('fecha_replan') if request.POST.get(
					'fecha_replan') != '' else '9999-12-31'), '%Y-%m-%d'),
				MOTIVO_REPLAN=(str(request.POST.get('motivo_replan'))),
				FECHA_STANDBY=datetime.strptime((request.POST.get('fecha_standby') if request.POST.get(
					'fecha_standby') != '' else '9999-12-31'), '%Y-%m-%d'),
				MOTIVO_STANDBY=(str(request.POST.get('motivo_standby'))))

			SeguiPryModelo.objects.create(
				PROYECTO_ID=data_act_pry.PROYECTO_ID,
				USUARIO_REPORTE=data_act_pry.USUARIO_REPORTE,
				FECHA_REPORTE=data_act_pry.FECHA_REPORTE,
				FASE_COMPRAS=data_act_pry.FASE_COMPRAS,
				FASE_PREPARACION=data_act_pry.FASE_PREPARACION,
				FASE_IMPLEMENTACION=data_act_pry.FASE_IMPLEMENTACION,
				FASE_PRUEBAS=data_act_pry.FASE_PRUEBAS,
				FASE_PRODUCCION=data_act_pry.FASE_PRODUCCION,
				SITUACION=data_act_pry.SITUACION,
				FECHA_REPLAN=data_act_pry.FECHA_REPLAN,
				MOTIVO_REPLAN=data_act_pry.MOTIVO_REPLAN,
				FECHA_STANDBY=data_act_pry.FECHA_STANDBY,
				MOTIVO_STANDBY=data_act_pry.MOTIVO_STANDBY)

			list_all_pry = ListPryModelo.objects.all().values('ID', 'PROYECTO_GCIA', 'GERENCIA')
			list_pry_act = ListPryModelo.objects.filter(ESTADO='activo').values('ID', 'PROYECTO_GCIA', 'GERENCIA')
			list_model_pry = ListPryModelo.objects.all()
			list_model_status = SeguiPryModelo.objects.select_related().all()

			return render(request, 'gcia_plan/red/servicios/prycore.html',
				{'list_all_pry': list_all_pry, 'list_pry_act': list_pry_act, 
				'list_model_pry': list_model_pry, 'list_model_status': list_model_status})

		except:
			return HttpResponse('<H1>ERROR</H1>')


# ##################### SMC #####################
# geolocator = Nominatim(user_agent='smc')
# prov_limite = { 'Misiones': ['Misiones','Corrientes'],
# 				'San Luis': ['San Luis','Cordoba','La Pampa','Mendoza','San Juan','La Rioja'],
# 				'San Juan': ['San Juan','La Rioja','San Luis','Mendoza'],
# 				'Entre Rios': ['Entre Rios','Corrientes','Santa Fe','Buenos Aires'],
# 				'Santa Cruz': ['Santa Cruz','Chubut'],
# 				'Rio Negro': ['Rio Negro','Chubut','Neuquen','La Pampa','Buenos Aires','Mendoza'],
# 				'Chubut': ['Chubut','Rio Negro','Santa Cruz'],
# 				'Cordoba': ['Cordoba','Santiago del Estero','Santa Fe','Buenos Aires','La Pampa','San Luis','La Rioja','Catamarca'],
# 				'Mendoza': ['Mendoza','San Juan','San Luis','La Pampa','Neuquen'],
# 				'La Rioja': ['La Rioja','Catamarca','Cordoba','San Luis','San Juan'],
# 				'Catamarca': ['Catamarca','Salta','Tucuman','Santiago del Estero','Cordoba','La Rioja'],
# 				'La Pampa': ['La Pampa','Cordoba','Buenos Aires','Rio Negro','Neuquen','San Luis'],
# 				'Santiago del Estero':['Santiago del Estero','Chaco','Santa Fe','Cordoba','Catamarca','Tucuman','Salta'],
# 				'Corrientes': ['Corrientes','Misiones','Chaco','Santa Fe','Entre Rios'],
# 				'Santa Fe': ['Santa Fe','Chaco','Corrientes','Entre Rios','Buenos Aires','Cordoba','Santiago del Estero'],
# 				'Tucuman': ['Tucuman','Salta','Santiago del Estero','Catamarca'],
# 				'Neuquen': ['Neuquen','Mendoza','La Pampa','Rio Negro'],
# 				'Salta': ['Salta','Jujuy','Formosa','Chaco','Santiago del Estero','Tucuman','Catamarca'],
# 				'Chaco': ['Chaco','Formosa','Corrientes','Santa Fe','Santiago del Estero','Salta'],
# 				'Formosa': ['Formosa','Salta','Chaco'],
# 				'Jujuy': ['Jujuy','Salta'],
# 				'Ciudad Autonoma de Buenos Aires': ['CABA','Buenos Aires'],
# 				'Buenos Aires': ['Buenos Aires','Entre Rios','Santa Fe','Cordoba','La Pampa','Rio Negro'],
# 				'Tierra del Fuego': ['Tierra del Fuego'],
# 				'todo': ['Misiones','San Luis','San Juan','Entre Rios','Santa Cruz','Rio Negro','Chubut','Cordoba','Mendoza','La Rioja',
# 						'Catamarca','La Pampa','Santiago del Estero','Corrientes','Santa Fe','Tucuman','Neuquen','Salta','Chaco','Formosa',
# 						'Jujuy','CABA','Buenos Aires','Tierra del Fuego']
# 			}


# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def listadoSitios(request):
# 	if request.method == 'GET':
# 		return render(request, "gcia_plan/red/servicios/smc.html")

# 	if request.method == 'POST':
# 		pedido = {"coord":None, 'prov':None , "maxResultados":None, "indoorsCheck":None}
# 		sitios = []
	
# 		if request.POST["coordenada1"]:
# 			pedido["coord"] = request.POST.get("coordenada1").strip()
# 			pedido["maxResultados"] = request.POST.get("maxBusquedas1",'5')
# 			pedido["indoorsCheck"] = request.POST.get("indoorsCheck1")
# 			try:
# 				pedido['prov'] = unidecode.unidecode(geolocator.reverse(pedido["coord"]).raw['address']['state'])
# 			except:
# 				pedido['prov'] = 'todo'
			
# 			fecha = request.POST.get("fecha")
			
# 			list_all_sitios = busquedaSitos(prov_limite[pedido['prov']], fecha, pedido["indoorsCheck"])

# 			for i in list_all_sitios:
# 				dist = geodesic('{0}, {1}' .format(i['LATITUD'], i['LONGITUD']), pedido["coord"]).kilometers
				
# 				if dist <= 15:
# 					i['DISTANCIA'] = dist

# 					if i['DISTANCIA'] <= 5:
# 						i['COBERTURA'] = 'Muy Buena'
# 					elif i['DISTANCIA'] <= 7:
# 						i['COBERTURA'] = 'Buena'
# 					elif i['DISTANCIA'] <= 10:
# 						i['COBERTURA'] = 'Baja'
# 					else:
# 						i['COBERTURA'] = 'Muy Baja'
					
# 					i['COORDENADA_BUSCADA'] = pedido["coord"]

# 					sitios.append(i)

# 			sitios.sort(key=lambda s: s['DISTANCIA'])
			
# 			try:
# 				resultSitios = [sitios[i] for i in range(0, int(pedido["maxResultados"]))]
			
# 			except:
# 				resultSitios = sitios				

# 			if len(resultSitios) != 0:
# 				list_sitios = []

# 				for i in resultSitios:
# 					list_sitios.append(i['SITIO'])
				
# 				resultCeldas = busquedaCeldas(list_sitios, fecha)
# 			else:
# 				resultCeldas = []
			
# 			return render(request, "gcia_plan/red/servicios/smc.html", {'result': 1, 'resultSitios':resultSitios, 'resultCeldas':resultCeldas})


# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def listadoMasivoSitios(request):
# 	if request.method == 'GET':
# 		return render(request, "gcia_plan/red/servicios/smcMasivo.html")

# 	if request.method == 'POST':
# 		myfile = request.FILES['file']
# 		filename = myfile.name
		
# 		doc = smcFileModel(DOC_SMC=myfile)
# 		doc.save()
		
# 		BASE_DIR = Path(__file__).resolve().parent.parent
# 		pathfile = '{0}/../../../media/gcia_plan/red/files/{1}' .format(BASE_DIR,filename)
				
# 		data = []
# 		resultSitiosTotal = []
# 		resultCeldasTotal = []

# 		data = pd.read_excel(pathfile,header=0).to_dict(orient='records')

# 		for i in range(0,len(data)):			
# 			data[i]['PROVINCIA']=unidecode.unidecode(geolocator.reverse('{0}, {1}' .format(data[i]['LATITUD'], data[i]['LONGITUD'])).raw['address']['state'])
# 			data[i]['FECHA_SOLICITADA']=data[i]['FECHA_SOLICITADA'].strftime('%Y-%m-%d')
		
# 		os.remove(pathfile)

# 		for datum in data:
# 			sitios = []
			
# 			list_all_sitios = busquedaSitos(prov_limite[datum['PROVINCIA']], datum['FECHA_SOLICITADA'], datum["INDOOR"])
			
# 			for i in list_all_sitios:
# 				dist = geodesic('{0}, {1}' .format(i['LATITUD'], i['LONGITUD']), '{0}, {1}' .format(datum['LATITUD'], datum['LONGITUD'])).kilometers
				
# 				if dist <= 15:
# 					i['DISTANCIA'] = dist

# 					if i['DISTANCIA'] <= 5:
# 						i['COBERTURA'] = 'Muy Buena'
# 					elif i['DISTANCIA'] <= 7:
# 						i['COBERTURA'] = 'Buena'
# 					elif i['DISTANCIA'] <= 10:
# 						i['COBERTURA'] = 'Baja'
# 					else:
# 						i['COBERTURA'] = 'Muy Baja'
					
# 					i['COORDENADA_BUSCADA'] = '{0}, {1}' .format(datum['LATITUD'], datum['LONGITUD'])

# 					sitios.append(i)

# 			sitios.sort(key=lambda s: s['DISTANCIA'])
			
# 			try:
# 				resultSitios = [sitios[i] for i in range(0, int(datum["CANTIDAD_DESEADOS"]))]
			
# 			except:
# 				resultSitios = sitios				

# 			if len(resultSitios) != 0:
# 				list_sitios = []

# 				for i in resultSitios:
# 					list_sitios.append(i['SITIO'])
				
# 				resultCeldas = busquedaCeldas(list_sitios, datum['FECHA_SOLICITADA'])
# 			else:
# 				resultCeldas = []

# 			resultSitiosTotal.append(resultSitios)
# 			resultCeldasTotal.append(resultCeldas)
		
# 		sitiosList=[]
# 		celdasList=[]
		
# 		for x in resultSitiosTotal:
# 			for i in x:
# 				sitiosList.append(i)
		
# 		for x in resultCeldasTotal:
# 			for i in x:
# 				celdasList.append(i)
		
# 		return render(request, "gcia_plan/red/servicios/smcMasivo.html", {'sitiosList':sitiosList, 'celdasList':celdasList, 'resultFlag':True})


# def busquedaSitos(provincias, fecha, chk_indoor):
# 	try:
# 		sql = """
# 				SELECT 
# 					sitio,
# 					Sitio_old,
# 					latitud, 
# 					longitud,
# 					provincia,
# 					es_indoor, 
# 					owner
# 				FROM (
# 					SELECT 
# 						Sitio_old,
# 						sitio, 
# 						latitud, 
# 						longitud,
# 						provincia,
# 						CASE 
# 							WHEN  regexp_instr(tipo_soluciones, 'M|W|B') != 0 THEN '' 
# 						ELSE 'SI'
# 						END es_indoor,  
# 						' ' owner
# 					FROM planing.spider_sitios
# 					WHERE 
# 						pais = 'ARGENTINA'
# 						AND provincia = '{0}'
# 						AND regexp_instr(Sitio_old,'COW|PR') = 0
# 						AND F_INICIO <= to_date('{1}','YYYY-MM-DD')
# 			"""
# 		if chk_indoor is not None:
# 			sql = sql + "\n AND regexp_instr(tipo_soluciones, 'M|W|B') != 0"
			
# 		sql = sql + """	
# 						UNION ALL
						
# 						SELECT 
# 							'' sitio_old,
# 							sitio_claro, 
# 							latitud, 
# 							longitud,
# 							provincia,
# 							'' es_indoor,
# 							'RSH -'|| ANFITRION OWNER
# 						FROM ( 
# 							SELECT 
# 								DISTINCT sitio_claro, 
# 								latitud, 
# 								longitud, 
# 								provincia,
# 								ANFITRION 
# 							FROM  planing.celdas_en_ransharing
# 							WHERE to_date('{1}','YYYY-MM-DD') BETWEEN f_inicio AND f_last_see 
# 								AND provincia = '{0}'
# 							) 
# 						)
# 					"""

# 		db = config('db_kraken_planing')
# 		conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 		c = conn.cursor()
		
# 		result = []
		
# 		for i in provincias:
# 			c.execute(sql .format(i.upper(),fecha))
# 			data = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
# 			result.extend(data)

# 		conn.close()

# 		return result

# 	except cx_Oracle.Error as e:
# 		error, = e.args
		
# 		print("#####  ERROR de cx_Oracle #####")
# 		print(error.code)
# 		print(error.message)

# 		raise e


# def busquedaCeldas(list_sitios, fecha):
# 	try:
# 		sql = """
# 				SELECT 
# 					decode(a.tecnologia,'L','4G','U','3G','G','2G','4G') TECNOLOGIA,
# 					a.SITIO_OLD U_TECNICA_OLD,
# 					a.cell_name_OLD NOMBRE_CELDA_OLD,
# 					b.sitio CELLID_NUEVO,
# 					a.cell_name BTS_NAME_NUEVO,
# 					a.cid,
# 					a.lac || a.tac LAC,
# 					b.nombre,
# 					b.localidad,
# 					b.departamento,
# 					b.provincia,
# 					nvl(b.direccion_calle,direccion_REF) Calle, 
# 					nvl(b.direccion_numero,'S/N') numero,
# 					b.latitud,
# 					b.longitud,
# 					replace(a.cobertura,'.',',') RADIO,
# 					a.azimuth,
# 					63 ANGULO,
# 					nvl(a.eutrancellid, '') eutrancellid
# 				FROM planing.spider_celdas a, planing.spider_sitios b
# 				WHERE a.sitio=b.sitio(+)
# 					AND b.pais in ('ARGENTINA',null)
# 					AND a.tipo_solucion!='N'
# 					AND b.sitio in ('{0}') 
# 				UNION ALL
# 				SELECT
# 					'4G' tecnologia,
# 					'' U_TECNICA_OLD,
# 					'' NOMBRE_CELDA_OLD,
# 					r.sitio_claro CELLID_NUEVO,
# 					r.celda_claro BTS_NAME_NUEVO,
# 					r.cid,
# 					to_char(r.tac) LAC,
# 					r.NOMBRE,
# 					r.localidad,
# 					r.departamento,
# 					r.provincia,
# 					r.calle, 
# 					nvl(r.numero,'S/N') numero,
# 					r.LATITUD, 
# 					r.LONGITUD,
# 					'' RADIO,
# 					to_char(r.azimuth) azimuth,
# 					63 ANGULO,
# 					to_char(r.eutracelid) eutrancellid
# 				FROM planing.celdas_en_ransharing r
# 				WHERE to_date('{1}','YYYY-MM-DD') BETWEEN f_inicio AND f_last_see
# 					AND sitio_claro in ('{0}') 
# 				ORDER BY tecnologia
# 			"""

# 		db = config('db_kraken_planing')
# 		conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 		c = conn.cursor()
		
# 		result = []
		
# 		for i in list_sitios:
# 			c.execute(sql .format(i,fecha))
# 			data = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
# 			result.extend(data)

# 		conn.close()

# 		return result
	
# 	except cx_Oracle.Error as e:
# 		error, = e.args
		
# 		print("#####  ERROR de cx_Oracle #####")
# 		print(error.code)
# 		print(error.message)

# 		raise e


# ##################### Visualizador de UTs #####################
# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def viewUT(request):
# 	if request.method == 'GET':
# 		return render(request, 'gcia_plan/red/servicios/utviewer.html')

# 	if request.method == 'POST':
# 		valor = (str(request.POST.get('valor')).strip())

# 		if '-' in valor:
# 			ut = utModel.objects.select_related().filter(ut__contains=valor)
			
# 			return render(request, 'gcia_plan/red/servicios/utviewer.html', {'ut':ut})
# 		else:
# 			if len(valor)==5:
# 				ut = utModel.objects.select_related().filter(cell_id__cell_id_old__contains=valor)

# 				return render(request, 'gcia_plan/red/servicios/utviewer.html', {'ut':ut})
# 			elif len(valor)==7:
# 				ut = utModel.objects.select_related().filter(cell_id__cell_id__contains=valor)

# 				return render(request, 'gcia_plan/red/servicios/utviewer.html', {'ut':ut})
# 			else:
# 				ut = utModel.objects.select_related().filter(cell_id__denominacion__contains=valor)
			
# 				return render(request, 'gcia_plan/red/servicios/utviewer.html', {'ut':ut})


# ##################### Busqueda de Sitios en Localidad #####################
# @csrf_exempt
# @require_http_methods(["GET","POST"])
# def viewSitiosLocal(request):
# 	if request.method == 'GET':
# 		db = config('db_kraken_planing')

# 		conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 		c = conn.cursor()

# 		c.execute("""
# 				SELECT * FROM ( 
# 					SELECT
# 						n_provincia provincia
# 					FROM sitios_loc)
# 				GROUP BY provincia
# 				ORDER BY provincia
# 				""")

# 		provincia = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 		c.execute("""
# 				SELECT * FROM ( 
# 					SELECT
# 						n_localidad localidad
# 					FROM sitios_loc)
# 				GROUP BY localidad
# 				ORDER BY localidad
# 				""")

# 		localidad = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
		
# 		return render(request, 'gcia_plan/red/servicios/sitiosLocal.html', {'provincia':provincia, 'localidad':localidad})
	
# 	if request.method == 'POST':
# 		pais = str(request.POST.get('pais'))
# 		provincia = str(request.POST.get('provincia'))
# 		localidad = str(request.POST.get('localidad'))

# 		db = config('db_kraken_planing')

# 		conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 		c = conn.cursor()
		
# 		c.execute("""
# 				SELECT 
# 					t.sitio_old,
# 					t.sitio,
# 					t.tipo_soluciones,
# 					t.tecnologias,
# 					t.nombre,
# 					t.activo,
# 					t.direccion_calle calle,
# 					t.direccion_numero numero,
# 					t.direccion_ref,
# 					t.LATITUD,
# 					t.LONGITUD,
# 					nvl(COUBICADO, 'Propio') COUBICADO,
# 					t.estructura_tipo,
# 					t.estructura_altura,
# 					t.estructura_camuflada,
# 					g.n_localidad localidad,
# 					TRANSLATE(UPPER(g.n_municipio),'ÁÉÍÓÚ','AEIOU') municipio,
# 					g.n_departamento DEPARTAMENTO,
# 					g.n_provincia provincia,
# 					g.n_pais_cod pais,
# 					t.estado_contrato,
# 					t.vto_ultimo_contrato vto_contrato
# 				FROM spider_sitios t, sitios_loc g
# 				WHERE 
# 					g.sitio=t.sitio AND
# 					g.n_pais_cod='{0}' AND
# 					g.n_provincia='{1}' AND
# 					g.n_localidad='{2}'
# 				""" .format(pais, provincia, localidad))

# 		sitios = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 		c.execute("""
# 				SELECT * FROM ( 
# 					SELECT
# 						n_provincia provincia
# 					FROM sitios_loc)
# 				GROUP BY provincia
# 				ORDER BY provincia
# 				""")

# 		provincia = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 		c.execute("""
# 				SELECT * FROM ( 
# 					SELECT
# 						n_localidad localidad
# 					FROM sitios_loc)
# 				GROUP BY localidad
# 				ORDER BY localidad
# 				""")

# 		localidad = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 		return render(request, 'gcia_plan/red/servicios/sitiosLocal.html', {'result':1, 'sitios':sitios, 'provincia':provincia, 'localidad':localidad})


# ##################### Busqueda de historico de celdas #####################
# @csrf_exempt
# @require_http_methods(["GET","POST"])
# def viewHistoricoCeldas(request):
# 	if request.method == 'GET':
# 		return render(request, 'gcia_plan/red/servicios/baseHistoricoCeldas.html')

# 	if request.method == 'POST':
# 		valor = str(request.POST.get('valor'))

# 		db = config('db_kraken_planing')

# 		conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 		c = conn.cursor()

# 		resultCeldasSpider = list()
# 		resultCeldasBaja = list()
# 		showspider = False
# 		showbaja = False

# 		if len(valor)==5:
# 			c.execute("""
# 					select * from (
# 						select cell_name, cell_name_old, sitio, sitio_old, 'baja' tabla from planing.historico_bajas_celdas
# 						union all
# 						select TO_NCHAR(cell_name), TO_NCHAR(cell_name_old), TO_NCHAR(sitio), TO_NCHAR(sitio_old), 'spider' tabla from planing.spider_celdas
# 					) where sitio_old= '{}'
# 					""" .format(valor))

# 			celdas = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
			
# 			for i in celdas:
# 				if i['TABLA']=='spider':
# 					resultCeldasSpider.append(celdaSpider(i['CELL_NAME']))
				
# 				elif i['TABLA']=='baja':
# 					resultCeldasBaja.append(celdaBaja(i['CELL_NAME']))

# 		elif len(valor)==7:
# 			c.execute("""
# 					select * from (
# 						select cell_name, cell_name_old, sitio, sitio_old, 'baja' tabla from planing.historico_bajas_celdas
# 						union all
# 						select TO_NCHAR(cell_name), TO_NCHAR(cell_name_old), TO_NCHAR(sitio), TO_NCHAR(sitio_old), 'spider' tabla from planing.spider_celdas
# 					) where sitio = '{}'
# 					""" .format(valor))

# 			celdas = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 			for i in celdas:
# 				if i['TABLA']=='spider':
# 					resultCeldasSpider.append(celdaSpider(i['CELL_NAME']))
				
# 				elif i['TABLA']=='baja':
# 					resultCeldasBaja.append(celdaBaja(i['CELL_NAME']))

# 		elif len(valor)==12:
# 			c.execute("""
# 					select * from (
# 						select cell_name, cell_name_old, sitio, sitio_old, 'baja' tabla from planing.historico_bajas_celdas
# 						union all
# 						select TO_NCHAR(cell_name), TO_NCHAR(cell_name_old), TO_NCHAR(sitio), TO_NCHAR(sitio_old), 'spider' tabla from planing.spider_celdas
# 					) where cell_name_old = '{}'
# 					""" .format(valor))

# 			celda = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
			
# 			if celda[0]['TABLA']=='spider':
# 				resultCeldasSpider.append(celdaSpider(celda[0]['CELL_NAME']))
			
# 			elif celda[0]['TABLA']=='baja':
# 				resultCeldasBaja.append(celdaBaja(celda[0]['CELL_NAME']))

# 		else:
# 			resultCeldasSpider.append(celdaSpider(valor))
# 			resultCeldasBaja.append(celdaBaja(valor))
		
# 		if len(resultCeldasSpider) > 0:
# 			showspider = True
		
# 		if len(resultCeldasBaja) > 0:
# 			showbaja = True

# 		return render(request, 'gcia_plan/red/servicios/baseHistoricoCeldas.html', 
# 			{'result': 1, 'showspider':showspider, 'showbaja':showbaja, 'resultCeldasSpider':resultCeldasSpider, 'resultCeldasBaja':resultCeldasBaja})


# def celdaSpider(celda):
# 	db = config('db_kraken_planing')

# 	conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 	c = conn.cursor()

# 	c.execute("""
# 			select 
# 				sc.CELL_NAME,
# 				sc.SITIO,
# 				sc.TECNOLOGIA,
# 				sc.AZIMUTH,
# 				sc.COBERTURA,
# 				ss.LATITUD,
# 				ss.LONGITUD,
# 				ss.LOCALIDAD,
# 				ss.PROVINCIA,
# 				ss.PAIS
# 			from planing.spider_celdas sc
# 			left JOIN planing.spider_sitios ss
# 				on (sc.sitio=ss.sitio) 
# 			where cell_name = '{}'
# 			""" .format(celda))
	
# 	celdas = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 	try:
# 		return celdas[0]
# 	except:
# 		return None


# def celdaBaja(celda):

# 	db = config('db_kraken_planing')

# 	conn = cx_Oracle.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
# 	c = conn.cursor()

# 	c.execute("""
# 			select * from planing.historico_bajas_celdas where cell_name = '{}'
# 			""" .format(celda))
	
# 	celdas = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

# 	try:
# 		return celdas[0]
# 	except:
# 		return None


# ##################### Busqueda de sitios por calle #####################
# @csrf_exempt
# @require_http_methods(["GET","POST"])
# def viewSitiosCalles(request):
# 	if request.method == 'GET':
# 		return render(request, 'gcia_plan/red/servicios/sitiosCalles.html')

# 	if request.method == 'POST':
# 		pais = 'Argentina'
# 		prov = str(request.POST.get('provincia'))
# 		local = str(request.POST.get('localidad'))

# 		calle1 = str(request.POST.get('calle1'))
# 		calle1Ni = int(request.POST.get('calle1Ni'))
# 		calle1Nf = int(request.POST.get('calle1Nf'))
# 		calle2 = str(request.POST.get('calle2'))
# 		if calle2 != '':
# 			calle2Ni = int(request.POST.get('calle2Ni'))
# 			calle2Nf = int(request.POST.get('calle2Nf'))
# 		calle3 = str(request.POST.get('calle3'))
# 		if calle3 != '':
# 			calle3Ni = int(request.POST.get('calle3Ni'))
# 			calle3Nf = int(request.POST.get('calle3Nf'))

# 		fecha = request.POST.get("fecha")

# 		numerosCalle1 = numerosCalle(calle1Ni,calle1Nf)
# 		if calle2 != '':
# 			numerosCalle2 = numerosCalle(calle2Ni,calle2Nf)
# 		if calle3 != '':
# 			numerosCalle3 = numerosCalle(calle3Ni,calle3Nf)

# 		listCoord1 = listCoordenadas(pais,prov,local,calle1,numerosCalle1)
# 		if calle2 != '':
# 			listCoord2 = listCoordenadas(pais,prov,local,calle2,numerosCalle2)
# 		if calle3 != '':
# 			listCoord3 = listCoordenadas(pais,prov,local,calle3,numerosCalle3)

# 		list_all_sitios = busquedaSitos(prov_limite[prov], fecha, chk_indoor=None)

# 		sitiosCalle1 = sitiosCalles(listCoord1,list_all_sitios)
# 		if calle2 != '':
# 			sitiosCalle2 = sitiosCalles(listCoord2,list_all_sitios)
# 		else:
# 			sitiosCalle2 = []
# 		if calle3 != '':
# 			sitiosCalle3 = sitiosCalles(listCoord3,list_all_sitios)
# 		else:
# 			sitiosCalle3 = []
				
# 		return render(request, "gcia_plan/red/servicios/sitiosCalles.html", {'result': 1, 'sitiosCalle1':sitiosCalle1, 'sitiosCalle2':sitiosCalle2, 'sitiosCalle3':sitiosCalle3})
	

# def numerosCalle(ni,nf):
# 	calles = list()

# 	while True:
# 		calles.append(str(ni))
# 		ni+=50
		
# 		if ni > nf:
# 			break
	
# 	return calles


# def listCoordenadas(pais,prov,local,calle,numeros):
# 	coordenadas = list()

# 	for i in numeros:
# 		location = geolocator.geocode("{4}, {3}, {2}, {1}, {0}" .format(pais,prov,local,calle,i))
		
# 		lat = location.raw['lat']
# 		lon = location.raw['lon']

# 		coordenadas.append({'calle': "{3} {4}, {2}, {1}, {0}" .format(pais,prov,local,calle,i), 'lat': lat,'lon': lon})
	
# 	return coordenadas


# def sitiosCalles(listCoord,list_all_sitios):
# 	sitios = list()
# 	sitiosFinal = list()

# 	for x in listCoord:
# 		for i in list_all_sitios:
# 			dist = geodesic('{0}, {1}' .format(i['LATITUD'], i['LONGITUD']), '{0}, {1}' .format(x['lat'], x['lon'])).kilometers
		
# 			if dist <= 15:
# 				i['DISTANCIA'] = dist

# 				if i['DISTANCIA'] <= 5:
# 					i['COBERTURA'] = 'Muy Buena'
# 				elif i['DISTANCIA'] <= 7:
# 					i['COBERTURA'] = 'Buena'
# 				elif i['DISTANCIA'] <= 10:
# 					i['COBERTURA'] = 'Baja'
# 				else:
# 					i['COBERTURA'] = 'Muy Baja'
				
# 				i['CALLE_BUSCADA'] = x['calle']

# 				sitios.append(i)

# 		sitios = [i for n, i in enumerate(sitios) if i not in sitios[n + 1:]]
		
# 		sitiosFinal.append(sitios)
# 	print(sitiosFinal)
# 	return sitiosFinal
			