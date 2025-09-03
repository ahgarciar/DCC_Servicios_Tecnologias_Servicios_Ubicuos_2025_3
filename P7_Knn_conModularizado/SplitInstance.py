import pandas as pd
import random

#La validacion split o dividida lo que hace es separar la instancia en dos conjuntos
# el primero de ellos de nombre entrenamiento y el segundo como validacion
# En este tipo de validacion usalmente se divide en 80/20, 90/10, 70/30 o 60/40
#   Depende de la cantidad de registros que tenga la instancia

def split_instance(instance, percentage):
    tot_reg_entrenamiento = int(percentage*len(instance)) #Ej. 70% de registros para entrenamiento
    tot_reg_validacion = len(instance) - tot_reg_entrenamiento

    indices = [i for i in range(len(instance))]

    random.seed(5)
    random.shuffle(indices)
    ####################

    entrenamiento = pd.DataFrame(columns=instance.columns)
    validacion = pd.DataFrame(columns=instance.columns)

    for i in range(0, tot_reg_entrenamiento):
        fila = instance.loc[[indices[i]]]
        entrenamiento = pd.concat([entrenamiento, fila])

    for i in range(tot_reg_entrenamiento, len(instance)):
        fila = instance.loc[[indices[i]]]
        validacion = pd.concat([validacion, fila])

    entrenamiento.reset_index(drop = True, inplace=True)
    validacion = validacion.reset_index(drop = True)

    return entrenamiento, validacion