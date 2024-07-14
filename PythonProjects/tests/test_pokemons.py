import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='5fa420c98164f4fc8c1448812028314b'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID=4572

def test_status_code():
    response=requests.get(url=f'{URL}/trainers',params={'trainer_id':TRAINER_ID} )
    assert response.status_code==200

def test_trainerid():
    response_get=requests.get(url=f'{URL}/trainers', params={'id':TRAINER_ID})
    assert response_get.json()['data'][1]['trainer_name']=='alinoch'