import random

#leemos el archivo
with open("nombres.txt", "r") as f:
    lista = f.read().split("\n")
    lista.pop()

#creamos una lista de nombres
nombres = []
for i in lista:
    nombres.append(i)

#nombre de entre 5 y 10 letras
def nombre():
    largo = random.randint(5, 10)
    nombre_1 = random.choice(nombres)
    nombre_2 = random.choice(nombres)
    nombre_3 = random.choice(nombres)
    partes = largo/3
    partes = int(partes)
    nombre = nombre_1[:partes] + nombre_2[:partes] + nombre_3[:partes]
    #si hay 3 silabas seguidas ponemos una vocal en medio
    silabas = ["a", "e", "i", "o", "u"]
    nombre = list(nombre)
    for i in range(len(nombre)-2):
        if nombre[i] not in silabas and nombre[i+1] not in silabas and nombre[i+2] not in silabas:
            nombre.insert(i+1, random.choice(silabas))
    nombre = "".join(nombre)
    if nombre[-1] not in silabas:
        nombre += random.choice(silabas)
    return nombre

print(nombre())