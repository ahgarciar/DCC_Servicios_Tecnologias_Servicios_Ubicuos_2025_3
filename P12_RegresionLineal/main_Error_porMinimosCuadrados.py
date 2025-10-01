
def error_cuadratico(y_referencia, y_constrate):
    error = 0
    for i in range(len(y_referencia)):
        aux = y_referencia[i] - y_constrate[i]
        aux = aux*aux
        error += aux
    return error

if __name__ == "__main__":
    X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Yprevista = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77]

    Yobservada = [2, 7, 12, 17, 23, 27, 32, 38, 44, 48, 54, 58, 64, 67, 73, 79]

    Yajustada = [2.8125, 7.8125, 12.8125, 17.8125, 22.8125, 27.8125, 32.8125, 37.8125,
                 42.8125, 47.8125, 52.8125, 57.8125, 62.8125, 67.8125, 72.8125, 77.8125]

    error_con_prevista = error_cuadratico(Yobservada, Yprevista)
    error_con_ajustada = error_cuadratico(Yobservada, Yajustada)

    print("error con prevista: " + str(error_con_prevista))
    print("error con ajustada: " + str(error_con_ajustada))
