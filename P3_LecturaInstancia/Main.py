
archivo = open("Instancia.csv")

contenido = archivo.readlines()
print(contenido)

instancia = [ list(map(int,registro.split(","))) for registro in contenido]
print(instancia)

print("Instancia:")
for registro in instancia:
    print(registro)
