import json

import pytest
import requests

from configs import SQLAlchemyConfig

fake_post = {'id': 9999, 'title': 'SomeCoolPost', 'tags': ['house'], 'content': 'London is the capital of Great Britain'}
user_id = 34

@pytest.fixture
def post():
    return fake_post


def test_get_post(post):
    requests.post(f'http://localhost:8000/users/{user_id}/posts/', json=post)
    resp = requests.get(f'http://localhost:8000/users/{user_id}/posts/9999')
    json_data = json.loads(resp.text)
    assert resp.status_code == 200
    assert json_data is not None


def test_update_post(post):
    post['title'] = 'Trips'
    resp = requests.put(f'http://localhost:8000/users/{user_id}/posts/9999', json=post)
    json_data = json.loads(resp.text)
    assert json_data is not None


def test_delete_post(post):
    requests.post(f'http://localhost:8000/users/{user_id}/posts/9999', json=post)
    resp = requests.delete(f'http://localhost:8000/users/{user_id}/posts/9999/')
    json_data = json.loads(resp.text)
    assert json_data is not None
