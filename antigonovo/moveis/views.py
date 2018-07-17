from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse

from antigonovo.moveis.models import Movel


def index(request):
    query_set = Movel.objects.order_by('titulo')
    ctx = {
        'moveis': list(query_set)
    }

    return render(request, 'moveis/index.html', context=ctx)


@login_required
def new(request):
    return render(request, 'moveis/movel_form.html')


@login_required
def create(request):
    dct = request.POST
    preco = dct['preco'].replace(',', '.')
    movel = Movel(titulo=dct['titulo'], preco=preco, descricao=dct['descricao'])
    movel.save()
    return redirect(reverse('moveis:index'))
