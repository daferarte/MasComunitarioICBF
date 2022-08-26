from django.urls import path
from . import views
from asistencia.views import listasdeasistencia

urlpatterns = [
    path('', listasdeasistencia, name="index"),
    path('inicio/', listasdeasistencia, name="inicio"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
