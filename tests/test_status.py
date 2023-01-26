import requests
import pytest

def test_states_code():
    response=requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200


def test_trainer_id():
    response=requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':'1885'})
    assert response.json()['trainer_name']=='Димас-расколбас'