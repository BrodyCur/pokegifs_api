import json
import requests
import os

key = os.environ.get("GIPHY_KEY")
url = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=charizard"

gifres = requests.get(url)
gif_body = json.loads(gifres.content)
print(gif_body)

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/") 
body = json.loads(res.content)
print(body["name"])
print(body["id"])
print(body["types"][0]["type"]["name"])
