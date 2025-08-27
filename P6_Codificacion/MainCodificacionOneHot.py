import pandas as pd

instancia = pd.read_csv("../Archivos/Instancia.csv")
print(instancia.head())

instancia_codificada = pd.get_dummies(instancia, columns=["Outlook","Temperature","Humidity","Wind"], dtype=int)

columnas = list(instancia_codificada.columns) #encabezados - nombres de las columnas

columna_a_mover = 'Play Tennis' #columna de la clase
columnas.pop(columnas.index(columna_a_mover))
columnas.insert(len(instancia_codificada)-1, columna_a_mover)
instancia_codificada = instancia_codificada[columnas]

print("Instancia:")
print(columnas) #encabezados
for i in range(0, len(instancia_codificada)):
    registro = instancia_codificada.loc[i].tolist()
    print(str(registro))

