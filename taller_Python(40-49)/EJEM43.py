capital = float(input("Capital actual: "))

if capital < 0:
    prestamo = 10000 - capital
    capital = 10000
elif capital <= 20000:
    prestamo = 20000 - capital
    capital = 20000
else:
    prestamo = 0

equipo = 5000
mobiliario = 2000
resto = capital - equipo - mobiliario
insumos = resto / 2
incentivos = resto / 2

print("Préstamo bancario:", prestamo)
print("Insumos:", insumos)
print("Incentivos:", incentivos)

#Capital actual: 5000
#Préstamo bancario: 15000.0
#Insumos: 4000.0
#Incentivos: 4000.0
