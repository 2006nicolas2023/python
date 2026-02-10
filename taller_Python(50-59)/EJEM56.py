dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

cociente = 0
resto = dividendo

while resto >= divisor:
    resto -= divisor
    cociente += 1

print("Cociente:", cociente)
print("Resto:", resto)

#Dividendo: 8
#Divisor: 2
#Cociente: 4
#Resto: 0
