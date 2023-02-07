#recolectamos todos los nombres
import requests
lista = []

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

for i in range(1, 964):
    pokemon_data = get_pokemon_data(i)
    nombre = pokemon_data["name"]
    #dividimos el nombre en palabras
    nombre = nombre.split(" ")
    nombre = nombre[0].split("-")
    #Si la primera palabra es mega quitamos la primera palabra
    if nombre[0] == "mega":
        nombre.pop(0)
    if nombre[0] not in lista:
        lista.append(nombre[0])
        print(nombre[0])
    else:
        print(nombre[0],"ya esta en la lista")

#Agregamos la lista de nombres a un archivo
with open("nombres.txt", "w") as f:
    for i in lista:
        f.write(i + "\n")

 