from os import path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from antigonovo.django_assertions import dj_assert_contains
from antigonovo.moveis.models import Movel


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('moveis:index'))


IMAGE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(IMAGE_PATH, 'prensa.jpg')


@pytest.fixture
def moveis(db):
    image = SimpleUploadedFile(
        name='prensa.jpg', content=open(IMAGE_PATH, 'rb').read(), content_type='image/jpeg')
    movel = Movel(
        titulo='Prensa de Madeira da Época Colonial',
        preco='30000.001',
        foto=image,
        descricao='Prensa de farinha de mandioca, madeira maciça. Construída artesanalmente por '
                  'escravos.'

    )

    movel.save()
    return [movel]


@pytest.fixture
def resp(client, moveis):
    return client.get(reverse('moveis:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        '30000,00',
        'Prensa de Madeira da Época Colonial',
        'Prensa de farinha de mandioca, madeira maciça. Construída artesanalmente por escravos.',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)


def test_image_url(resp, moveis):
    movel = moveis[0]
    dj_assert_contains(resp, movel.foto.url)
