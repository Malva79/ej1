from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
# esta es la base del conjunto de rutas o la raiz de las rutas
# aca se manejan las rutas o ENDsPOINTS que pueda tener tu API
router.register(r'programmers', views.ProgrammerViewSet)
# la r permite que no se interprete como un salto de linea o como un escape de caracter
# usamos la r para indicar que no tome los caracteres como \n o \tque es un salto de linea o una tabulacion, es un formato tipo RAW de python.
# 'programmers' es un ENDPOINT

urlpatterns = [  # la ruta base va a incluir todo los elementos que tenga el router que hemos creado en URLS
                 # esta es la lista de URLS que maneja ROUTER en sus elementos URLS
    path('', include(router.urls)),
    path('', views.programmer, name='inicio'),
]
# Ahora incluimos o agregamos esta URLS en las vistas del proyecto (url.py de drf)
