#! /usr/bin/env python3              #Shebang

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# My eyes! The goggles do nothing! from challenge

eyes1 = challenge[2][1]
goggles1 = challenge[2][0]
nothing1 = challenge[-1]

print(f"My {eyes1} The {goggles1} do {nothing1}!")

#From the trial list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:

eyes2 = trial[2].get("goggles")
goggles2 = trial[2].get("eyes")
nothing2 = trial[-1]

print(f"My {eyes2} The {goggles2} do {nothing2}!")

#From the nightmare list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:


eyes3 = nightmare[0].get("user").get("name").get("first")
goggles3 = nightmare[0].get("kumquat")
nothing3 = nightmare[0].get("d")

print(f"My {eyes3} The {goggles3} do {nothing3}!")





