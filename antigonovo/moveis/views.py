from django.shortcuts import render

# Create your views here.
from antigonovo.moveis.models import Movel


def index(request):
    query_set = Movel.objects.order_by('titulo')
    ctx = {
        'moveis': list(query_set)
    }

    return render(request, 'moveis/index.html', context=ctx)
