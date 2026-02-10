A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

N = A * 1000 + B * 100 + C * 10 + D
redondeado = round(N, -2)

print("Número:", N)
print("Redondeado:", redondeado)

#A: 2
#B: 3
#C: 6
#D: 2
#Número: 2362
#Redondeado: 2400
