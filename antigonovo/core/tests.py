import pytest

from antigonovo.django_assertions import dj_assert_contains


def test_home_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Antigo Novo Móveis',
        'contato@antigonovo.com.br',
        '+55 12 987654-3210',
        'href="/contato/"'

    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)


def test_contact_status_code(client):
    response = client.get('/contato/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        '(12) 98873-9669',
        '(12) 98802-1263',
        '(12) 99799-1571',
        'SP 50 (estrada SJC / Monteiro Lobato) Nº 20.200, KM 20',
        'São José dos Campos - SP',
        '12220-340',
    ]
)
def test_contact_content(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
