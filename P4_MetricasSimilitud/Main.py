
def hamming(vectorA, vectorB):
    distancia = 0
    for i in range(len(vectorA)):
        if  vectorA[i] != vectorB[i]:
            distancia += 1
    return distancia

import pandas as pd

instancia = pd.read_csv("../Archivos/Instancia.csv")
print(instancia.head())

registro = instancia.loc[0].tolist()
print(registro)

print("Registros a comparar:")
for i in range(1, len(instancia)):
    reg_a_comparar = instancia.loc[i].tolist()
    d = hamming(registro[0:-1], reg_a_comparar[0:-1])
    print(str(reg_a_comparar) + "distancia: " + str(d))

