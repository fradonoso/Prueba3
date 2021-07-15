from core.models import Mascota
from core.forms import MascotaForm
from django.shortcuts import render, redirect

# Create your views here.

def home(request):

    mascota = Mascota.objects.all()
    datos ={
        'mascota':mascota
    }
    return render(request, 'core/home.html', datos)

def form_mascota(request):

    datos = {
        'form':MascotaForm()
    }
    if request.method == 'POST':
        formulario = MascotaForm(request.POST)

        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = 'Mascota guardada correctamente'

    return render(request, 'core/form_mascota.html',  datos)

def form_mod_mascota(request, id):

    mascota = Mascota.objects.get(idMascota=id)

    datos = {
        'form': MascotaForm(instance = mascota)
    }

    if request.method =='POST':
        formulario = MascotaForm(data=request.POST, instance = mascota)

        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] =  "Mascota Modificada correctamente"

    return render(request, 'core/form_mod_mascota.html', datos)

def form_del_mascota(request, id):
    mascota = Mascota.objects.get(idMascota = id)
    mascota.delete()

    return redirect(to="home")