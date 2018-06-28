from decimal import Decimal

from django.shortcuts import render

# Create your views here.
from antigonovo.moveis.models import Movel


def index(request):
    description = 'Prensa de farinha de mandioca, madeira maciça. Construída artesanalmente por ' \
                  'escravos.'
    ctx = {
        'moveis':
            [
                Movel(
                    'Prensa de Madeira da Época Colonial',
                    Decimal('30000.00'),
                    description
                ),
                Movel(
                    'Mesa',
                    Decimal('4000.00'),
                    'Mesa em madeira de lei'
                ),
            ]
    }

    return render(request, 'moveis/index.html', context=ctx)
