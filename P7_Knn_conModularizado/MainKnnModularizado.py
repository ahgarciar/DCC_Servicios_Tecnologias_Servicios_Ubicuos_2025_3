import LoadInstance
import SplitInstance
import Knn


instancia = LoadInstance.load()
print(instancia.head())

entrenamiento, validacion = SplitInstance.split_instance(instancia, 0.7)

#import math as m
#k = int(m.sqrt(len(entrenamiento)))  # valor entero de la raiz cuadrada del total de registros

for k in range(1, len(entrenamiento)):
    print("con k = " + str(k))

    TP = 0
    FN = 0
    FP = 0
    TN = 0

    respKnn = [] #yPred

    #registro a clasificar
    for index in range(len(validacion)):
        reg = validacion.loc[index].tolist()

        resp = Knn.exect_knn(entrenamiento, reg, k)

        respKnn.append(resp)

    respVerdaderas = list(validacion["Play Tennis"])

    for i in range(len(respKnn)):
        if respVerdaderas[i] == "Yes":
            if respKnn[i] == "Yes":
                TP += 1
            else: #No
                FN += 1
        else: #NO
            if respKnn[i] == "Yes":
                FP += 1
            else: #No
                TN += 1


    print("Total de registros para validar: " + str(len(validacion)))
    print("Registros correctamente clasificados:" + str(TP+TN))

    eficiencia = (TP+TN)/(TP+TN+FP+FN)
    precision = TP/(TP+FP)
    recall  = TP/(TP+FN)
    specificity = TN/(TN+FP)
    f1_score = 2* ((precision*recall)/(precision+recall))

    print("Eficiencia: " + str(eficiencia))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("Specificity: " + str(specificity))
    print("F1_Score: " + str(f1_score))