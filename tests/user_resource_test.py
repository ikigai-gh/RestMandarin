import json

import pytest
import requests

from configs import SQLAlchemyConfig

fake_user = {'id': 9999, 'name': 'John', 'email': 'john@foo.com', 'phone': '+11111111111'}

@pytest.fixture
def user():
    return fake_user


def test_get_user(user):
    requests.post('http://localhost:8000/users/', json=user)
    resp = requests.get('http://localhost:8000/users/9999')
    json_data = json.loads(resp.text)
    assert resp.status_code == 200
    assert json_data is not None


def test_update_user(user):
    user['name'] = 'Bob'
    resp = requests.put('http://localhost:8000/users/9999', json=user)
    json_data = json.loads(resp.text)
    assert json_data is not None


def test_delete_user(user):
    requests.post('http://localhost:8000/users/', json=user)
    resp = requests.delete('http://localhost:8000/users/9999')
    json_data = json.loads(resp.text)
    assert json_data is not None
