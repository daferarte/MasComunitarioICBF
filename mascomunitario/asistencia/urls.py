from django.urls import path
from . import views


urlpatterns = [
    path('asistencia/', views.listasdeasistencia, name="Asistencia"),
    path('registrohorario/', views.registroHorario, name="registro"),
    path('masivo/', views.guardarDatos, name="masivo"),
    path('listaencuentros/', views.VerHorarios, name="encuentros"),
    path('actasistencia/<int:horario_id>', views.ActListasAsistencia, name="ActAsistencia"),
]
