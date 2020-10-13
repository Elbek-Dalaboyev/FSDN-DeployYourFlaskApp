'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'myjwtsecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDM4MTc5OTQsIm5iZiI6MTYwMjYwODM5NCwiZW1haWwiOiJkYWxhYm95ZXZlQGdtYWlsLmNvbSJ9.9R3EjNNR27onjrY9jkn5nuriCf35bQGmeX41rZqnwck'
EMAIL = 'dalaboyeve@gmail.com'
PASSWORD = 'believer_0'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
    assert False
