cantidad = int(input("Cantidad en bolívares: "))

billetes = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 50, 20, 10]

for b in billetes:
    cant = cantidad // b
    cantidad %= b
    print(f"{b}: {cant}")

#Cantidad en bolívares: 78630
#50000: 1
#20000: 1
#10000: 0
#5000: 1
#2000: 1
#1000: 1
#500: 1
#100: 1
#50: 0
#20: 1
#10: 1
