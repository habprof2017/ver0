from django.shortcuts import render
# from .forms import NotaModelForm
from .models import Nota


def inicio(request):
    todaslasNotas = Nota.objects.all()
    titulo = 'Hola desconocido'
    vacio = '-'
    if request.user.is_authenticated():
        titulo = 'Hola %s' % (request.user)
    # form = NotaModelForm(request.POST or None)
    context = {
        "notas": todaslasNotas,
        "un_titulo": titulo,
        "vacio": vacio,
    }

    # if form.is_valid():
    #   instance = form.save(commit=False)
    #  	instance.save()

    return render(request, 'mesaentrada/mesaentrada_index.html', context)

# poner el nombre del usuario arriba
# cambiar el contexto
# mostar toda la lista ?
