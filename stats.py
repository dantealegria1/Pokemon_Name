import random
import requests

def estadisticas():
    ataque = random.randint(1, 120)
    defensa = random.randint(1, 120)
    hp = random.randint(1, 120)
    sp_atk = random.randint(1, 120)
    sp_def = random.randint(1, 120)
    speed = random.randint(1, 120)
    return ataque, defensa, hp, sp_atk, sp_def, speed

def Tipo():
    tipo1 = random.randint(1, 18)
    url = f"https://pokeapi.co/api/v2/type/{tipo1}"
    response = requests.get(url)
    tipo1 = response.json()
    tipo1 = tipo1["name"]
    return tipo1

def moveset():
    moveset = []
    for i in range(4):
        move = random.randint(1, 900)
        moveset.append(move)
    url = f"https://pokeapi.co/api/v2/move/{moveset[0]}"
    response = requests.get(url)
    move1 = response.json()
    move1 = move1["name"]
    url = f"https://pokeapi.co/api/v2/move/{moveset[1]}"
    response = requests.get(url)
    move2 = response.json()
    move2 = move2["name"]
    url = f"https://pokeapi.co/api/v2/move/{moveset[2]}"
    response = requests.get(url)
    move3 = response.json()
    move3 = move3["name"]
    url = f"https://pokeapi.co/api/v2/move/{moveset[3]}"
    response = requests.get(url)
    move4 = response.json()
    move4 = move4["name"]
    return move1, move2, move3, move4

def abilies():
    ability = random.randint(1, 290)
    url = f"https://pokeapi.co/api/v2/ability/{ability}"
    response = requests.get(url)
    ability = response.json()
    ability = ability["name"]
    return ability

print(Tipo())