categoria = int(input("Categoría (1-4): "))
sueldo = float(input("Sueldo actual: "))

if categoria == 1:
    aumento = 0.15
elif categoria == 2:
    aumento = 0.10
elif categoria == 3:
    aumento = 0.08
elif categoria == 4:
    aumento = 0.05
else:
    aumento = 0

nuevo_sueldo = sueldo + sueldo * aumento

print("Categoría:", categoria)
print("Nuevo sueldo:", nuevo_sueldo)

#Categoría (1-4): 1
#Sueldo actual: 50000
#Categoría: 1
#Nuevo sueldo: 57500.0
