
def mse(y_real, y_estimada):
    error = 0
    n = len(y_real)
    for i in range(n):
        aux = y_real[i] - y_estimada[i]
        aux = aux*aux
        error += aux
    error = error/n #promedio
    return error

def rmse(y_real, y_estimada):
    error = mse(y_real, y_estimada)
    error = error ** (1/2) #raiz cuadrada
    return error

def mae(y_real, y_estimada):
    error = 0
    n = len(y_real)
    for i in range(n):
        aux =  abs(y_real[i] - y_estimada[i])
        error += aux
    error = error / n  # promedio
    return error


def mape(y_real, y_estimada):
    error = 0
    n = len(y_real)
    for i in range(n):
        aux = y_real[i] - y_estimada[i]
        aux = abs(aux/y_real[i])
        error += aux
    error = error * 100 / n  # promedio
    return error