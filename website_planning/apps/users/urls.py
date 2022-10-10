from django.urls import path
from apps.users.views import *


urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('login/', login_view, name="logInUser"),
    path('logout/', logout_view, name="logOutUser"),
    ]