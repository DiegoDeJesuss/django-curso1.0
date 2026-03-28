from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def cadastro(request):
    return HttpResponse('Ola mundo')

def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        queixa = request.POST.get('queixa')
        
        
        if len(nome) <= 2:
            return redirect('clientes')
        
        if queixa not in {'D', 'A'}:
            return redirect('clientes')
        
        return HttpResponse(f'{nome}, {email}, {queixa}')

