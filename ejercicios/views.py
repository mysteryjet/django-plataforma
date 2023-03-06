from django.shortcuts import render, get_object_or_404
from .models import Ejercicios

# Create your views here.

def render_ejercicios(request):
    ejercicios = Ejercicios.objects.all()
    return render(request, 'ejercicios.html', {'ejercicios':ejercicios})

def ejercicio_detail(request, ejercicio_id):
    ejercicio = get_object_or_404(Ejercicios, pk=ejercicio_id)
    return render(request, 'ejercicio_detail.html',{'ejercicio':ejercicio})