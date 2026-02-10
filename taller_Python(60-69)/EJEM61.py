a = int(input("Número 1: "))
b = int(input("Número 2: "))

resultado = 0

while a > 0:
    if a % 2 != 0:
        resultado += b
    a //= 2
    b *= 2

print("Resultado:", resultado)

#Número 1: 25
#Número 2: 7
#Resultado: 175
