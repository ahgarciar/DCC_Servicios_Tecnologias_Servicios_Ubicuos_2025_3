def hamming(vectorA, vectorB):
    distancia = 0
    for i in range(len(vectorA)):
        if  vectorA[i] != vectorB[i]:
            distancia += 1
    return distancia


def exect_knn(entrenamiento, registro, k):

    entrenamiento["distancia"] = -1

    # print("Registros a comparar:")
    for i in range(0, len(entrenamiento)):
        reg_a_comparar = entrenamiento.loc[i].tolist()
        d = hamming(registro[0:-1], reg_a_comparar[0:-1])
        # print(str(reg_a_comparar) + "distancia: " + str(d))

        entrenamiento.loc[
            i, "distancia"] = d  # modicar el registro en la columna "distancia" para agregarle el valor calculado

    entrenamiento = entrenamiento.sort_values(by="distancia", ascending=True)

    entrenamiento = entrenamiento.reset_index(drop=True)

    clasesK = []
    for i in range(0, k):
        clase = entrenamiento.loc[i, "Play Tennis"]
        clasesK.append(clase)
    # print(clasesK)

    import statistics
    moda = statistics.mode(clasesK)
    # print("La etiqueta asignada es: " + moda)

    return moda