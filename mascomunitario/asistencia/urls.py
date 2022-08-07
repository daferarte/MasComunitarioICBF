from django.urls import path
from . import views

urlpatterns = [
    path('asistencia/', views.listasdeasistencia, name="Asistencia"),
    path('registrohorario/', views.registroHorario, name="registro"),
]