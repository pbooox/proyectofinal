from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #url('pelicula/nueva/', views.pelicula_nueva, name='pelicula_nueva'),
    path('', views.home, name='home'),
    path('cli/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('cli/mandar/<int:pk>/', views.mandar_cliente, name='mandar_cliente'),
    path('bebida/nueva/<int:pk>/', views.nueva_bebida, name='nueva_bebida'),
    path('ing/nuevo/', views.nuevo_ingrediente, name='nuevo_ingrediente'),
    path('ing/', views.ingredientes , name='ingredientes'),
    path('ing/<int:pk>/editar', views.editar_ingrediente, name='editar_ingrediente'),
    path('ing/<pk>/borrar', views.borrar_ingrediente, name='borrar_ingrediente'),
    path('cli/', views.clientes , name='clientes'),
    ]