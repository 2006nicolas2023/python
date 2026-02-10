nombres = ["Show1", "Show2"]
ingresos = [5000, 3000]
gastos = [6000, 2000]
max_entradas = 400
vendidas = [450, 300]

for i in range(2):
    if gastos[i] > ingresos[i]:
        print("Pérdida:", nombres[i])

ganancias = [ingresos[i]-gastos[i] for i in range(2)]
print("Mayor ganancia:", nombres[ganancias.index(max(ganancias))])

if any(v > max_entradas for v in vendidas):
    print("Se vendieron más entradas de lo permitido")

#Pérdida: Show1
#Mayor ganancia: Show2
#Se vendieron más entradas de lo permitido
