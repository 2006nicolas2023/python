capital = float(input("Ingrese el capital del préstamo: "))
interes = float(input("Ingrese los intereses pagados: "))
tiempo = 4  # años

razon = (interes * 100) / (capital * tiempo)

print("Porcentaje anual cobrado:", razon, "%")

#Ingrese el capital del préstamo: 500000
#Ingrese los intereses pagados: 100000
#Porcentaje anual cobrado: 5.0 %
