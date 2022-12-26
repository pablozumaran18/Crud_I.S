from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [ "nombre", "patente_vehiculo", "hora_ingreso", "hora_salida"]
        widgets ={

             
            "nombre":forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre completo del cliente "}),
            "patente_vehiculo":forms.TextInput(attrs={"class":"form-control","placeholder":"Patente del vehiculo"}),
            "hora_ingreso":forms.TimeInput(attrs={"class":"form-control","placeholder":"Hora de ingreso"}),
            "hora_salida":forms.TimeInput(attrs={"class":"form-control","placeholder":"Hora de salida"}),
        }


class CalzoForm(forms.ModelForm):
    class Meta:
        model = Calzo
        fields = ["numero_estacionamiento", "tipo_vehiculo", "estado","cliente","nivel_estacionamiento"]
        widgets ={
 
            "numero_estacionamiento":forms.NumberInput(attrs={"class":"form-control","placeholder":"Numero de calzo"}),
            "tipo_vehiculo":forms.SelectMultiple(attrs={"class":"form-control"}),
            "estado":forms.Select(attrs={'class':'form-control',"placeholder":"Estado actual del calzo"}),
            "cliente":forms.Select(attrs={"class":"form-control","placeholder":"Cliente que esta utilizando el calzo"}),
            "nivel_estacionamiento":forms.Select(attrs={"class":"form-control","placeholder":"Nivel de calzo"}),
        }

class TipovehiculoForm(forms.ModelForm):
    class Meta:
        model = Tipovehiculo
        fields = [ "tipo_segmento"]
        widgets ={
            "tipo_segmento":forms.TextInput(attrs={"class":"form-control","placeholder":"Tipo de segmento admitido "}),
        }