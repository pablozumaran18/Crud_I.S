"""estacionamientos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("calzo_list/",CalzoListView.as_view(), name="calzo_list"),
    path("calzo_register/",CalzoCreate.as_view(), name="calzo_register"),
    path("calzo_deleted/<str:pk>/",CalzoDelete.as_view(), name="calzo_deleted"),
    path("calzo_edit/<str:pk>/",CalzoUpdate.as_view(), name="calzo_edit"),

#_____________________________

    path("cliente_list/",ClienteListView.as_view(), name="cliente_list"),
    path("cliente_register/",ClienteCreate.as_view(), name="cliente_register"),
    path("cliente_deleted/<str:pk>/",ClienteDelete.as_view(), name="cliente_deleted"),
    path("cliente_edit/<str:pk>/",ClienteUpdate.as_view(), name="cliente_edit"),

#_________________________________________________________________________________

    path("tipovehiculo_list/",TipovehiculoListView.as_view(), name="tipovehiculo_list"),
    path("tipovehiculo_register/",TipovehiculoCreate.as_view(), name="tipovehiculo_register"),
    path("tipovehiculo_deleted/<str:pk>/",TipovehiculoDelete.as_view(), name="tipovehiculo_deleted"),
    path("tipovehiculo_edit/<str:pk>/",TipovehiculoUpdate.as_view(), name="tipovehiculo_edit"),
]
