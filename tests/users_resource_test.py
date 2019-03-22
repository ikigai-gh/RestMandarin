import json

import pytest
import requests

from configs import SQLAlchemyConfig

fake_user = {'id': 9999, 'name': 'John', 'email': 'john@foo.com', 'phone': '+11111111111'}
filters_uri = 'id__exact=9999&id__gte=9998&name__exact=John&email__exact=john@foo.com&phone=+11111111111'


@pytest.fixture
def user():
    return fake_user


def setup_function():
    SQLAlchemyConfig.make_config()


def test_get_users():
    resp = requests.get('http://localhost:8000/users/')
    assert resp.status_code == 200
    assert resp.content is not None


def test_post_user(user):
    resp = requests.post('http://localhost:8000/users/', json=user)
    assert resp.status_code == 201


def test_pagination_get_users():
    limit = 100
    offset = 10
    resp = requests.get(f'http://localhost:8000/users?limit={limit}&offset={offset}')
    json_data = json.loads(resp.text)
    assert resp.status_code == 200
    assert len(json_data) == limit
    assert json_data[0]['id'] == offset + 1


def test_filters_get_users(user):
    requests.post('http://localhost:8000/users/', json=user)
    resp = requests.get(f'http://localhost:8000/users?{filters_uri}')
    json_data = json.loads(resp.text)
    assert resp.status_code == 200
    assert len(json_data) == 1
