import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7c07e4c76a98856184e422fceec3a121'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
 
body_new_pokemons = {
    "name": "generate",
    "photo_id": -1
}

body_edit = {
    "pokemon_id": "165480",
    "name": "IDE",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "165480"
}

response_new_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_new_pokemons)
print(response_new_pokemons.text)
message = response_new_pokemons.json()['message']
print(message)


edit_pokemons = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit)
print(edit_pokemons.text)


pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(pokeball.text)