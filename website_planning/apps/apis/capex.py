from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
import psycopg2
from apps.basedata.config import config
import json
import datetime


def myconverter(data):
    if isinstance(data, datetime.datetime):
        return data.__str__() 


@api_view(['GET'])
@permission_classes([])
def baseCapex(self):
    '''
    Json que entrega informacion de la tabla BASE_CAPEX.
    '''
    db = config('db_kraken_planing')
    
    try:
        conn = psycopg2.connect(db["user"],db["passw"],db["host"]+"/"+db["database"])
        c = conn.cursor()
        
        c.execute("""
                SELECT * FROM BASE_CAPEX
                """)

        base_capex = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]

        conn.close()
        
        return HttpResponse(json.dumps(base_capex,indent=4,default=myconverter),content_type='application/json')
    
    except Exception as error:
        print(error)
