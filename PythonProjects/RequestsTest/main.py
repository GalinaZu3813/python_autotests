import requests
URL='https://api.pokemonbattle.ru/v2'
TOKEN='5fa420c98164f4fc8c1448812028314b'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
body_pokemons={
    "name": "Lauffy",
    "photo_id": 38
}
body_confirmation={'trainer_token': TOKEN}

'''response_pokemons=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemons)
print(response_pokemons.text)''''''покемон создан'''

'''pokemon_id=response_pokemons.json()['id']
print(pokemon_id)'''

'''message=response_pokemons.json()['message']
print(message)'''

body_putpokemons={
    "pokemon_id": "43381",
    "name": "Piter",
    "photo_id": 39
}

'''response_pokemons=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_putpokemons)
print(response_pokemons.text)''''''покем изменен'''

body_pokeboll={
    "pokemon_id": "43390"
}
'''response_pokemons=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeboll)
print(response_pokemons.text)''' '''покемон пойман в покебол'''


