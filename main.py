import requests
import json

token='7b600b42bcc0d28ebcd7cc062760cbf5'

response_create = requests.post('https://pokemonbattle.me:5000/pokemons',json={
        "name": "Bocchi",
        "photo": ""
    }, 
    headers={
        'Content-Type': 'application/json',
        'trainer_token':token
    }
)

print(response_create.text)
pokemon_id = response_create.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons',json={
        "pokemon_id": pokemon_id,
        "name": "The Rock",
        "photo": "https://pbs.twimg.com/media/Fict6WtX0AAi6pG.png"
    },
    headers={
        'Content-Type':'application/json',
        'trainer_token':token
    }
)

print(response_change.text)

response_catch = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',json={
        "pokemon_id": pokemon_id,
    },
    headers={
        'Content-Type':'application/json',
        'trainer_token':token
    }
)

print(response_catch.text)