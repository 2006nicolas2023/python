libros = int(input("Cantidad libros: "))
ciencia = romance = 0

for i in range(libros):
    genero = input("Género: ")
    paginas = int(input("Páginas: "))

    if genero == "ciencia ficcion":
        ciencia += 1
    if genero == "romance":
        romance += 1

print("Libros ciencia ficción:", ciencia)
print("Libros romance:", romance)
print("Porcentaje ciencia ficción:", (ciencia/libros)*100)


#Cantidad libros: 2
#Páginas libro: 200
#Páginas libro: 150
#Total páginas: 350
