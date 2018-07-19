from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse

from antigonovo.moveis.forms import MovelForm
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
    form = MovelForm(request.POST)
    # Valide os Inputs
    if not form.is_valid():
        ctx = {'form': form}
        return render(request, 'moveis/movel_form.html', context=ctx, status=400)
    # Se válido, salve no banco e redirecione
    dct = form.cleaned_data
    movel = Movel(**dct)
    movel.save()
    return redirect(reverse('moveis:index'))
