import pytest
from django.urls import reverse

from antigonovo.django_assertions import dj_assert_contains


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('moveis:index'))


@pytest.fixture
def resp(client):
    return client.get(reverse('moveis:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        '//s3.amazonaws.com/img.iluria.com/product/466341/A93300/450xN.jpg',
        'R$ 30.000,00',
        'Prensa de Madeira da Época Colonial',
        'Prensa de farinha de mandioca, madeira maciça. Construída artesanalmente por escravos.',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)
