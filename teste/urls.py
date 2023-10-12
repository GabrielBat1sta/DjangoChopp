from django.urls import path
from . import views

urlpatterns = [
    path('/templates/', views.PaginaInicial, name='pagina_inicial'),
    path('', include('teste.urls')),
]
