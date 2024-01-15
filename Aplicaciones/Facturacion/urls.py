from django.urls import path
from . import views
urlpatterns=[
path('',views.listadoProvincias),
path('guardarProvincia/',views.guardarProvincia),
path('eliminarProvincia/<id>',views.eliminarProvincia),
path('editarProvincia/<id>',views.editarProvincia),
path ('procesarActualizacionProvincia/', views.procesarActualizacionProvincia)



]
