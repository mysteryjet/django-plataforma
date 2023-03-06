from django.urls import path
from .views import render_ejercicios, ejercicio_detail

app_name = 'ejercicios'

urlpatterns = [
    path('',render_ejercicios, name='ejercicios'),
    path('<int:ejercicio_id>',ejercicio_detail,name = 'ejercicio_detail')
]