from reservas.forms import Form_reserva
from reservas.models import Reserva
from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, 'Lista_reservas.html')

def Actualizar_res(request,id):
    res = Reserva.objects.get(id = id)
    formulario = Form_reserva(instance=res)
    if request.method == 'POST':
        formulario = Form_reserva(request.POST, instance=res)
        if formulario.is_valid():
            formulario.save()
        return index(request)
    data = {'formulario':formulario}
    return render(request,'Añadir_Reserva.html',data)

def Añadri_res(request):
    formulario = Form_reserva()
    if request.method == 'POST':
        formulario = Form_reserva(request.POST)
        if formulario.is_valid():
            formulario.save()
        return index(request)
    data = {'formulario' : formulario}
    return render(request, 'Añadir_Reserva.html', data)

def Eliminar_res(request,id):
    res = Reserva.objects.get(id = id)
    res.delete()
    return redirect('/')

def lista_res(request):
    list_reserva = Reserva.objects.all()
    data = {'list_reserva': list_reserva}
    return render(request, 'Lista_reservas.html', data)

