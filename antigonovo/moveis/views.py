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
    # Extraia os dados do request
    dct = request.POST
    # Valide os Inputs
    erros = {}
    for propriedade in 'titulo descricao'.split():
        if dct.get(propriedade, '') == '':
            erros[propriedade] = 'Campo obrigatório.'
    preco = dct['preco'].replace(',', '.')
    try:
        float(preco)
    except Exception:
        erros['preco'] = 'Digite um valor numérico'
    # Se tiver erro, retorne para o form preenchendo com dados já enviados e msgs de erro
    if erros:
        ctx = {'form': dct, 'erros': erros}
        return render(request, 'moveis/movel_form.html', context=ctx, status=400)
    # Se válido, salve no banco e redirecione
    movel = Movel(titulo=dct['titulo'], preco=preco, descricao=dct['descricao'])
    movel.save()
    return redirect(reverse('moveis:index'))
