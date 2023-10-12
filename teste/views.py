from django.shortcuts import render

def PaginaInicial(request):
    return render(request, 'pagina_inicial.html')