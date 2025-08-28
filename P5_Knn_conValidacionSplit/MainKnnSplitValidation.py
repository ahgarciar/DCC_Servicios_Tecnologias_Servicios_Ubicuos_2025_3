
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

indices = [i for i in range(len(instancia))]
import random
random.shuffle(indices)
####################

entrenamiento = pd.DataFrame(columns=instancia.columns)
validacion = pd.DataFrame(columns=instancia.columns)

for i in range(0, tot_reg_entrenamiento):
    fila = instancia.loc[[indices[i]]]
    entrenamiento = pd.concat([entrenamiento, fila])

for i in range(tot_reg_entrenamiento, len(instancia)):
    fila = instancia.loc[[indices[i]]]
    validacion = pd.concat([validacion, fila])

entrenamiento.reset_index(drop = True, inplace=True)
validacion = validacion.reset_index(drop = True)

#registro a clasificar
for index in range(len(validacion)):
    registro = validacion.loc[index].tolist()
    print(registro)

    import math as m
    k = int(m.sqrt(len(entrenamiento))) #valor entero de la raiz cuadrada del total de registros

    entrenamiento["distancia"] = -1

    #print("Registros a comparar:")
    for i in range(0, len(entrenamiento)):
        reg_a_comparar = entrenamiento.loc[i].tolist()
        d = hamming(registro[0:-1], reg_a_comparar[0:-1])
        #print(str(reg_a_comparar) + "distancia: " + str(d))

        entrenamiento.loc[i, "distancia"] = d #modicar el registro en la columna "distancia" para agregarle el valor calculado

    entrenamiento = entrenamiento.sort_values(by="distancia", ascending=True)

    entrenamiento = entrenamiento.reset_index(drop=True)

    clasesK = []
    for i in range(0, k):
        clase = entrenamiento.loc[i, "Play Tennis"]
        clasesK.append(clase)
    #print(clasesK)

    import statistics
    moda = statistics.mode(clasesK)
    print("La etiqueta asignada es: " + moda)