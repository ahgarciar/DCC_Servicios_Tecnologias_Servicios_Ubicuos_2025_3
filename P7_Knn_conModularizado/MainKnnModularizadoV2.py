import LoadInstance
import SplitInstance
import Knn

instancia = LoadInstance.load()
print(instancia.head())

entrenamiento, validacion = SplitInstance.split_instance(instancia, 0.7)

import math as m
k = int(m.sqrt(len(entrenamiento)))  # valor entero de la raiz cuadrada del total de registros

print("con k = " + str(k))

respKnn = [] #yPred

#registro a clasificar
for index in range(len(validacion)):
    reg = validacion.loc[index].tolist()

    resp = Knn.exect_knn(entrenamiento, reg, k)

    respKnn.append(resp)

respVerdaderas = list(validacion["Play Tennis"])

from sklearn.metrics import classification_report
reporte = classification_report(
    respVerdaderas, respKnn, target_names=["Clase A", "Clase B"],
    output_dict=True
)
print(reporte)

#print("Total de registros para validar: " + str(len(validacion)))
print("Eficiencia:" + str(reporte["accuracy"]))
