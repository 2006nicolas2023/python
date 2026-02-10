contador = 0
num = 1

while contador < 3:
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if suma == num:
        print("Número perfecto:", num)
        contador += 1
    num += 1
#Número perfecto: 6
#Número perfecto: 28
#Número perfecto: 496
