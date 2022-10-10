from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
import psycopg2
from apps.basedata.config import config
import json


@api_view(['GET'])
@permission_classes([])
def sitios_onair(self):
    '''
    Json que mustra cantidad de sitios on-air.
    '''
    db = config('db_kraken_planing')
    
    try:
        conn = psycopg2.connect(dbname=db["database"], user=db["user"], 
                                password=db["password"], host=db['host'], port=db['port'])
        c = conn.cursor()
        
        c.execute("""
                SELECT * FROM sitios
                """)

        cantidad_sitios = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

        conn.close()
        
        return HttpResponse(json.dumps(cantidad_sitios, indent=4), content_type='application/json')

    except Exception as error:
        print(error)


# @api_view(['GET'])
# @permission_classes([])
# def G5(self):
#     '''
#     Json que mustra cantidad de cobertura on-air por tecnologia y localidades.
#     '''
#     db = config('db_kraken_planing')

#     try:
#         conn = psycopg2.connect(dbname=db["database"], user=db["user"],
#                                 password=db["password"], host=db['host'], port=db['port'])
#         c = conn.cursor()

#         c.execute("""
#                     with  estatus_2022 as(
#                         select *
#                         from (
#                             SELECT s.sitio,
#                                     s.CAGGR,
#                                     s.tipo_tx,
#                                     case when substr(lz.CELDA,8,1) = 'N' then 1 end NR_5G,      
#                                     case when substr(lz.CELDA,8,1) = 'D' then 1 end DSS_5G,
#                                     s.MACRO
#                                     FROM planing.spider_sitios s, rfweb.VW_CELDAS_5G@ledzite.world lz
#                             where ( activo=1 and regexp_instr(sitio,'COW|PR') = 0 and s.sitio = lz.CELL_ID(+))
#                             )
#                         GROUP BY SITIO, CAGGR, TIPO_TX, NR_5G, DSS_5G, MACRO
#                         ),
#                         sitios as (
#                             SELECT 
#                                 sitio,
#                                 pais 
#                             FROM spider_sitios 
#                             WHERE activo = 1 AND regexp_instr(sitio,'COW|PR') = 0)
#                     SELECT * FROM (
#                         SELECT   
#                             'MACRO' Tipo_solucion,
#                             sitios.pais,
#                             count(es_22.NR_5G) NR_5G, 
#                             count(es_22.DSS_5G) DSS_5G
#                         FROM sitios, estatus_2022 es_22 
#                         WHERE sitios.sitio = es_22.sitio(+) AND es_22.MACRO = '1' 
#                         GROUP BY sitios.pais
#                     )
#                 """)

#         G5 = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

#         conn.close()

#         return HttpResponse(json.dumps(G5, indent=4), content_type='application/json')

#     except Exception as error:
#         print(error)


# @api_view(['GET'])
# @permission_classes([])
# def poblacionCubierta(self):
#     '''
#     Json que mustra cantidad de cobertura on-air por tecnologia y localidades.
#     '''
#     db = config('db_kraken_planing')

#     try:
#         conn = psycopg2.connect(db["user"], db["passw"], db["host"]+"/"+db["database"])
#         c = conn.cursor()

#         c.execute("""
#                 SELECT
#                     pais_cod pais,
#                     COUNT(poblacion_total) ciudades_total,
#                     SUM(poblacion_total) poblacion_total,
#                     COUNT(CASE WHEN NVL(gsm,0)+NVL(umts,0)+NVL(lte,0)= 0 THEN 1 ELSE NULL END) Ciudades_SC,
#                     SUM(CASE WHEN NVL(gsm,0)+NVL(umts,0)+NVL(lte,0)= 0 THEN poblacion_total ELSE NULL END) Poblacion_SC
#                 FROM v_cobertura_tecnologias
#                 WHERE loc_nombre != 'ANTARTIDA'
#                 GROUP BY pais_cod
#                 """)

#         pob_cub = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

#         conn.close()

#         return HttpResponse(json.dumps(pob_cub, indent=4), content_type='application/json')

#     except Exception as error:
#         print(error)