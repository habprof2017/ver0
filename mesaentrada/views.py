from django.shortcuts import render


def inicio(request):
    return render(request, 'mesaentrada/mesaentrada_index.html', {})
