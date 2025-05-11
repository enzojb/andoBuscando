from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from apps.contador.views import contador_datos
urlpatterns=[
    path('datos/', contador_datos, name='contador_datos'),
    ]