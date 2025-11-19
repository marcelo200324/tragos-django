from django.shortcuts import render, get_object_or_404
from .models import Trago

def index(request):
    query = request.GET.get('q', '')  # obtener búsqueda
    if query:
        # Buscar en nombre y preparación
        tragos = Trago.objects.filter(
            nombre__icontains=query
        ) | Trago.objects.filter(
            preparacion__icontains=query
        )
    else:
        tragos = Trago.objects.all()  # mostrar todos si no hay búsqueda

    return render(request, 'core/index.html', {'tragos': tragos, 'query': query})

def detalle_trago(request, pk):
    trago = get_object_or_404(Trago, pk=pk)
    # apuntamos a detalle.html en lugar de detalle_trago.html
    return render(request, 'core/detalle.html', {'trago': trago})

