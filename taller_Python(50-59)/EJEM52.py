ninos = []
jovenes = []
adultos = []
viejos = []

cantidad = int(input("Cantidad de personas: "))

for i in range(cantidad):
    edad = int(input("Edad: "))
    peso = float(input("Peso: "))

    if edad <= 12:
        ninos.append(peso)
    elif edad <= 18:
        jovenes.append(peso)
    elif edad <= 60:
        adultos.append(peso)
    else:
        viejos.append(peso)

print("Promedio niños:", sum(ninos)/len(ninos))
print("Promedio jóvenes:", sum(jovenes)/len(jovenes))
print("Promedio adultos:", sum(adultos)/len(adultos))
print("Promedio viejos:", sum(viejos)/len(viejos))

#Cantidad de personas: 3
#Edad: 10
#Peso: 30
#Edad: 25
#Peso: 70
#Edad: 65
#Peso: 68
#Promedio niños: 30.0
#Promedio jóvenes: error
#Promedio adultos: 70.0
#Promedio viejos: 68.0
