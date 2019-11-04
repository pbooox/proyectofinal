from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages
from .models import Cliente, Bebida, DetalleBebida, Ingrediente
from .forms import FormCli, FormIng, BebidaForm

def home(request):
    return render(request,'bar/home.html')

def nuevo_cliente(request):
    if request.method == "POST":
        formulario = FormCli(request.POST)
        if formulario.is_valid():
            cli = formulario.save(commit=False)
            cli.save()
            return redirect('mandar_cliente', pk=cli.pk)
    else:
        formulario = FormCli()
    return render(request, 'bar/nuevo_cliente.html', {'formulario': formulario}) 

def nuevo_ingrediente(request):
    if request.method == "POST":
        formulario = FormIng(request.POST)
        if formulario.is_valid():
            ing = formulario.save(commit=False)
            ing.save()
    else:
        formulario = FormIng()
    return render(request, 'bar/nuevo_ingrediente.html', {'formulario': formulario})

def mandar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        formulario = BebidaForm(request.POST, instance=cliente)
        if formulario.is_valid():
            bebida = Bebida.objects.create(cliente=formulario.cleaned_data['cliente'])
            for ingrediente_id in request.POST.getlist('ingredientes'):
                detallebebida = DetalleBebida(ingrediente_id=ingrediente_id, bebida_id = bebida.id)
                detallebebida.save()
            messages.add_message(request, messages.SUCCESS, 'bebida Guardada Exitosamente')
    else:
        formulario = BebidaForm()
    return render(request, 'bar/nueva_bebida.html', {'formulario': formulario})
    

def nueva_bebida(request, pk):
    cli = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        formulario = BebidaForm(request.POST, instance=cli)
        if formulario.is_valid():
            bebida = Bebida.objects.create(cliente=formulario.cleaned_data['cliente'])
            for ingrediente_id in request.POST.getlist('ingredientes'):
                detallebebida = DetalleBebida(ingrediente_id=ingrediente_id, bebida_id = bebida.id)
                detallebebida.save()
            messages.add_message(request, messages.SUCCESS, 'bebida Guardada Exitosamente')
    else:
        formulario = BebidaForm()
    return render(request, 'bar/nueva_bebida.html', {'formulario': formulario})

def ingredientes(request):
    ings = Ingrediente.objects.all()
    return render(request, 'bar/ingredientes.html', {'ings': ings})

def editar_ingrediente(request, pk):
    ing = get_object_or_404(Ingrediente, pk=pk)
    if request.method == "POST":
        formulario = FormIng(request.POST, instance=ing)
        if formulario.is_valid():
            ing = formulario.save(commit=False)
            ing.save()
            return redirect('ingredientes')
    else:
        formulario = FormIng(instance=ing)
    return render(request, 'bar/nuevo_ingrediente.html', {'formulario': formulario})

def borrar_ingrediente(request, pk):
    ing = get_object_or_404(Ingrediente, pk=pk)
    ing.delete()
    return redirect('ingredientes')

def clientes(request):
    clis = Cliente.objects.all()
    return render(request, 'bar/clientes.html', {'clis': clis})

def bebidas(request):
    bebs = Bebida.objects.all()
    return render(request, 'bar/bebidas.html', {'bebs': bebs})

def detalle_bebida(request, pk):
    ing = Ingrediente.objects.filter(bebida=pk)
    return render(request, 'bar/detalle_bebida.html', {'ing': ing})
