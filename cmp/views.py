from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from bases.views import SinPrivilegios
from .models import Proveedor
from cmp.forms import ProveedorForm

import json


# Create your views here.

# INICIA VISTAS PROVEEDOR
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    permission_required = "cmp.view_proveedor"


class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


def proveedorInactivar(request, id):
    template_name = "cmp/inactivar_prv.html"
    contexto = {}
    prov = Proveedor.objects.filter(pk=id).first()

    if not prov:
        # return redirect("cmp:proveedor_list")
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj': prov}

    if request.method == 'POST':
        prov.estado = False
        prov.save()
        contexto = {'obj': 'OK'}
        return HttpResponse('Proveedor Inactivado ')

    return render(request, template_name, contexto)
