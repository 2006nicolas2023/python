nombres = ["Ana", "Luis", "Carlos"]
edades = [30, 25, 50]

prom = sum(edades) / len(edades)

print("Promedio edad:", prom)
print("Más joven:", nombres[edades.index(min(edades))])
print("Más viejo:", nombres[edades.index(max(edades))])

print("Profesores > promedio:", sum(1 for e in edades if e > prom))
print("Profesores < promedio:", sum(1 for e in edades if e < prom))

#Promedio edad: 35.0
#Más joven: Luis
#Más viejo: Carlos
#Profesores > promedio: 1
#Profesores < promedio: 2
