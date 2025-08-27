
def hamming(vectorA, vectorB):
    distancia = 0
    for i in range(len(vectorA)):
        if  vectorA[i] != vectorB[i]:
            distancia += 1
    return distancia

import pandas as pd

instancia = pd.read_csv("../Archivos/Instancia.csv")
print(instancia.head())

#registro a clasificar
registro = ["Rain","Mild","High","Weak","Yes"]
print(registro)

import math as m
k = int(m.sqrt(len(instancia))) #valor entero de la raiz cuadrada del total de registros

instancia["distancia"] = -1

print("Registros a comparar:")
for i in range(0, len(instancia)):
    reg_a_comparar = instancia.loc[i].tolist()
    d = hamming(registro[0:-1], reg_a_comparar[0:-1])
    print(str(reg_a_comparar) + "distancia: " + str(d))

    instancia.loc[i, "distancia"] = d #modicar el registro en la columna "distancia" para agregarle el valor calculado

instancia = instancia.sort_values(by="distancia", ascending=True)

instancia = instancia.reset_index(drop=True)

clasesK = []
for i in range(0, k):
    clase = instancia.loc[i, "Play Tennis"]
    clasesK.append(clase)
print(clasesK)

import statistics
moda = statistics.mode(clasesK)
print("La etiqueta asignada es: " + moda)