sueldo = float(input("Sueldo mensual de cada vendedor: "))
ventas1 = float(input("Ventas departamento 1: "))
ventas2 = float(input("Ventas departamento 2: "))
ventas3 = float(input("Ventas departamento 3: "))

total_ventas = ventas1 + ventas2 + ventas3

def pago(ventas):
    if ventas > total_ventas * 0.33:
        return sueldo * 1.20
    else:
        return sueldo

print("Departamento 1 recibe:", pago(ventas1))
print("Departamento 2 recibe:", pago(ventas2))
print("Departamento 3 recibe:", pago(ventas3))

#Sueldo mensual de cada vendedor: 1000
#Ventas departamento 1: 4000
#Ventas departamento 2: 3000
#Ventas departamento 3: 2000
#Departamento 1 recibe: 1200.0
#Departamento 2 recibe: 1000.0
#Departamento 3 recibe: 1000.0
