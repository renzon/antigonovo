import pytest

from antigonovo.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Antigo Novo Móveis',
        'contato@antigonovo.com.br',
        '+55 12 987654-3210',

    ]
)
def test_home(client, content):
    response = client.get('/')

    dj_assert_contains(response, content)
