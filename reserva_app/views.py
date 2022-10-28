from django.shortcuts import render,redirect
from reserva_app.models import reserva
from reserva_app.forms import FormReserva


# Create your views here.

def index(request):
    return render(request, 'index.html')

def listareserva(request):
    reservas=reserva.objects.all()
    data={'reservas':reservas}
    return render(request,'reserva.html',data)

def agregarreserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)

def eliminarreserva(request,id):
    res=reserva.objects.get(id=id)
    res.delete()
    return redirect('/reservas')

def actualizarreserva(request,id):
    res=reserva.objects.get(id=id)
    form = FormReserva(instance=res)
    if request.method == 'POST':
        form = FormReserva(request.POST,instance=res)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)


