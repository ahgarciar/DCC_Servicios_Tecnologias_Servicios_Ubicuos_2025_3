
def hamming(vectorA, vectorB):
    distancia = 0
    for i in range(len(vectorA)):
        if  vectorA[i] != vectorB[i]:
            distancia += 1
    return distancia

import pandas as pd

instancia = pd.read_csv("../Archivos/Instancia_completa.csv")
print(instancia.head())

#La validacion split o dividida lo que hace es separar la instancia en dos conjuntos
# el primero de ellos de nombre entrenamiento y el segundo como validacion
# En este tipo de validacion usalmente se divide en 80/20, 90/10, 70/30 o 60/40
#   Depende de la cantidad de registros que tenga la instancia

tot_reg_entrenamiento = int(0.70*len(instancia)) #70% de registros para entrenamiento
tot_reg_validacion = len(instancia) - tot_reg_entrenamiento

############################

#estratificacion-balanceo...
# cuantos registros tengo de cada clase
# tratar de que entre entrenamiento y validacion se tenga un equilibrio entre la cantidad
# de registros por clase
"""
0
1
2
3
.
.
.
13
"""
############################

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