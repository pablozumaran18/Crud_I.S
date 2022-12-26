from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


def home (request):
    return render(request,"core/home.html")

class CalzoListView(ListView):
    model = Calzo


class CalzoCreate(CreateView):
    model = Calzo
    form_class = CalzoForm
    success_url = reverse_lazy("calzo_list") 

class CalzoUpdate(UpdateView):
    model = Calzo
    form_class = CalzoForm
    template_name_suffix = "_update_form"
    

    def get_success_url(self):
        return reverse_lazy("calzo_list") 


class CalzoDelete(DeleteView):
    model = Calzo
    
    success_url = reverse_lazy("calzo_list") 



#_______________________________________________________

class ClienteListView(ListView):
    model = Cliente


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente_list") 

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = "_update_form"
    

    def get_success_url(self):
        return reverse_lazy("cliente_list") 


class ClienteDelete(DeleteView):
    model = Cliente
    
    success_url = reverse_lazy("cliente_list")


#__________________________________________________

class TipovehiculoListView(ListView):
    model = Tipovehiculo


class TipovehiculoCreate(CreateView):
    model = Tipovehiculo
    form_class = TipovehiculoForm
    success_url = reverse_lazy("tipovehiculo_list") 

class TipovehiculoUpdate(UpdateView):
    model = Tipovehiculo
    form_class = TipovehiculoForm
    template_name_suffix = "_update_form"
    

    def get_success_url(self):
        return reverse_lazy("tipovehiculo_list") 


class TipovehiculoDelete(DeleteView):
    model = Tipovehiculo
    
    success_url = reverse_lazy("tipovehiculo_list")