from django.shortcuts import render
from apps.main.models import *
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

session = requests.Session()
session.trust_env = False


@csrf_exempt
@require_http_methods(["GET"])
def inicio(request):
    return render(request, 'main/inicio.html')


@csrf_exempt
@require_http_methods(["GET"])
def gciaPlanCapex(request):
    return render(request, 'gcia_plan/capex/jefCapex.html')


@csrf_exempt
@require_http_methods(["GET"])
def gciaPlanMateriales(request):
    return render(request, 'gcia_plan/materiales/jefMate.html')


@csrf_exempt
@require_http_methods(["GET"])
def gciaPlanRed(request):
    return render(request, 'gcia_plan/red/jefRed.html')


@csrf_exempt
@require_http_methods(["GET"])
def nosotros(request):
    return render(request, 'main/nosotros.html')


@csrf_exempt
@require_http_methods(["GET","POST"])
def contacto(request):
    if request.method == 'GET':
        return render(request, 'main/contacto.html')

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')
        from_email = name+' '+'<'+request.POST.get('email')+'>'
        msj = 'Mensaje de '+from_email+':\n\t\t'+message

        if subject and message and from_email:
            try:
                email = EmailMessage(subject,message,from_email,
                        ['rd.pablo@gmail.com'])
                email.send(fail_silently=False)

                return render(request, 'main/gracias.html')


            except BadHeaderError:
                return HttpResponse('Invalid header found.')


@csrf_exempt
@require_http_methods(["GET"])
def gracias(request):
    if request.method == 'GET':
        return render(request, 'main/gracias.html')
