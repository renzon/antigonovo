import pytest
from django.urls import reverse

from antigonovo.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('login'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content',
    [
        '<form method="post"',
        '<button type="submit"',
        '<input type="email" name="username"',
        '<input type="password" name="password"',
    ]
)
def test_content(content, resp):
    dj_assert_contains(resp, content)


def test_login_action_link(resp):
    login_path = reverse('login')
    dj_assert_contains(resp, f'action="{login_path}"')


def test_forgot_password_link(resp):
    dj_assert_contains(resp, reverse('password_reset'))
