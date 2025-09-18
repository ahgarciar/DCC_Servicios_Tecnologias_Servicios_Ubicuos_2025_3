import pandas as pd

def load(name = "Instancia_completa.csv"):
    instancia = None

    if name!="":
        instancia = pd.read_csv("../Archivos/" + name, header=None)

    return instancia