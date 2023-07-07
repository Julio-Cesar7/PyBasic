# https://pokeapi.co/api/v2/pokemon/charizard

# https://pokeapi.co

import requests as rq

pokemon = input("Ingrese su pokemon")
res = rq.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon))

print(res.status_code)
# print(res.headers)

json = res.json()
print("JSON: {}".format(json))

