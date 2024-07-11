#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)

    sprites = pokeapi.get("sprites").get("front_default")
    
    print(sprites)

    moves = pokeapi.get("moves")[move]

    for item in moves:
        print(item)

    




main()
