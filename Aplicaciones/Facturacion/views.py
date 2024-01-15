from django.shortcuts import render, redirect
from .models import Provincia
from django.contrib import messages
# Create your views here.
def listadoProvincias(request):
    restauramteBdd=Provincia.objects.all()
    return render(request,"listadoProvincias.html",{'provincias':restauramteBdd})
def guardarProvincia(request):
    region_ed = request.POST["region_ed"]
    nombre_ed = request.POST["nombre_ed"]
    capital_ed = request.POST["capital_ed"]
    prefijo_ed = request.POST["prefijo_ed"]

    nuevaProvincia = Provincia.objects.create(region_ed=region_ed, nombre_ed=nombre_ed, capital_ed=capital_ed, prefijo_ed=prefijo_ed)

    messages.success(request, 'Provincia Guardada Exitosamente')
    return redirect('/')
def eliminarProvincia(request, id):
    provinciaEliminar = Provincia.objects.get(id_ed=id)
    provinciaEliminar.delete()
    messages.success(request, 'Provincia Eliminada Exitosamente')
    return redirect('/')

def editarProvincia(request, id):
    provinciaEditar = Provincia.objects.get(id_ed=id)
    return render(request, 'editarProvincia.html', {'provincia': provinciaEditar})


def procesarActualizacionProvincia(request):
    id_ed = request.POST["id"]
    region_ed = request.POST["region_ed"]
    nombre_ed = request.POST["nombre_ed"]
    capital_ed = request.POST["capital_ed"]
    prefijo_ed = request.POST["prefijo_ed"]

    # Obtener la provincia a editar
    provinciaEditar = Provincia.objects.get(id_ed=id_ed)

    # Actualizar los datos de la provincia
    provinciaEditar.region_ed = region_ed
    provinciaEditar.nombre_ed = nombre_ed
    provinciaEditar.capital_ed = capital_ed
    provinciaEditar.prefijo_ed = prefijo_ed

    # Guardar los cambios
    provinciaEditar.save()

    messages.success(request, 'Provincia Actualizada Exitosamente')
    return redirect('/')
