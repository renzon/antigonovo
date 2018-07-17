import pytest
from django.test import Client
from django.urls import reverse

from antigonovo.moveis.models import Movel


@pytest.fixture
def resp_without_user(client: Client):
    return client.get(
        reverse('moveis:create'),
        data={
            'titulo': 'Prensa',
            'preco': '3000,00',
            'descricao': 'Prensa do século passado',
        }
    )


@pytest.fixture
def user(django_user_model):
    usr = django_user_model(name='Renzo')
    usr.save()
    return usr


@pytest.fixture
def resp(user, client: Client):
    client.force_login(user)
    return resp_without_user(client)


def test_status_code_user_not_logged(resp_without_user):
    assert resp_without_user.url.startswith(reverse('login'))


def test_status_code_user_logged(resp):
    assert resp.url.startswith(reverse('moveis:index'))


def test_movel_salvo(resp):
    assert Movel.objects.exists()
