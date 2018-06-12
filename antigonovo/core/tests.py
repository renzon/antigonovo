from antigonovo.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


def test_home(client):
    response = client.get('/')
    dj_assert_contains(response, 'Olá Mundo')
