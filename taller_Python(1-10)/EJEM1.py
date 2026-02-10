edades = []

for i in range(3):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad)

promedio = sum(edades) / len(edades)

print("El promedio de edades es:", promedio)

#edades guarda las 3 edades
#sum(edades) suma todas
#len(edades) cuenta cuántas hay

#---------------------------------------------------------#
#Ingrese la edad 1: 18
#Ingrese la edad 2: 20
#Ingrese la edad 3: 22
#El promedio de edades es: 20.0