
archivo = open("datos_temperatura.txt")

contenido = archivo.readlines()

print(contenido)


datos = list(map(int, contenido))

print(datos)

suma = sum(datos)
print(suma)

