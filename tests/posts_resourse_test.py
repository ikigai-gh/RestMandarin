import json

import pytest
import requests

from configs import SQLAlchemyConfig

fake_post = {'id': 9999, 'title': 'SomeCoolPost', 'tags': ['house'], 'content': 'London is the capital of Great Britain'}
filters_uri = 'id__exact=9999&id__gte=9998&title__exact=SomeCoolPost&tags__in=house&content__in=London'
user_id = 34

@pytest.fixture
def post():
    return fake_post


def setup_function():
    SQLAlchemyConfig.make_config()


def test_get_posts():
    resp = requests.get(f'http://localhost:8000/users/{user_id}/posts/')
    assert resp.status_code == 200
    assert resp.content is not None


def test_post_post(post):
    resp = requests.post(f'http://localhost:8000/users/{user_id}/posts/', json=post)
    assert resp.status_code == 201


def test_pagination_get_posts():
    limit = 1
    offset = 0
    resp = requests.get(f'http://localhost:8000/users/{user_id}/posts?limit={limit}&offset={offset}')
    json_data = json.loads(resp.text)
    assert resp.status_code == 200
    assert len(json_data) == limit


def test_filters_get_posts(post):
    requests.post('http://localhost:8000/users/{user_id}/posts/', json=post)
    resp = requests.get(f'http://localhost:8000/users/{user_id}/posts?{filters_uri}')
    json_data = json.loads(resp.text)
    assert resp.status_code == 200
    assert len(json_data) == 1
