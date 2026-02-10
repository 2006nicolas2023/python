for i in range(5):
    nombre = input("Nombre: ")
    suma = 0
    for j in range(10):
        suma += float(input("Peso báscula: "))
    promedio = suma / 10
    anterior = float(input("Peso anterior: "))

    if promedio > anterior:
        print("SUBIÓ", promedio - anterior)
    else:
        print("BAJÓ", anterior - promedio)

#Peso anterior: 70
#Peso actual: 68
#BAJÓ 2.0
