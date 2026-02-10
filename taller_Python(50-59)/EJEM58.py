capital = float(input("Capital: "))
tasa = float(input("Tasa: "))
semanas = int(input("Semanas: "))

dias = semanas * 7

for i in range(dias):
    interes = capital * tasa / 365
    capital += interes

print("Capital final:", capital)

#Capital: 1000
#Tasa: 0.06
#Semanas: 1
#Capital final: 1001.15
