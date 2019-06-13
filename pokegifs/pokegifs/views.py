import json
import requests
import os
from django.http import JsonResponse, HttpResponseNotFound
# from django.shortcuts import render
from random import randint
import pdb

def poke_response(request, id):
    api_url = f"http://pokeapi.co/api/v2/pokemon/{id}/"
    res = requests.get(api_url)
    if res.status_code != 200:
        return JsonResponse({"error": "pokemon not found"}, status=404)
    body = json.loads(res.content)
    pokedex_id = body['id']
    name = body['name']
    types = []

    for t in body["types"]:
        types.append(t["type"]["name"])

    gif_key = os.environ.get("GIPHY_KEY")
    gif_res = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={gif_key}&q={name}")
    if gif_res.status_code != 200:
        return JsonResponse({"error": "Problem with api key."}, status=404)
    gif_body = json.loads(gif_res.content)
    gif_index = randint(0,len(gif_body["data"])-1)
    gif_url = gif_body["data"][gif_index]["url"]

    context = {
        "id": pokedex_id,
        "name": name,
        "types": types,
        "gif": gif_url
    }

    return JsonResponse(context)