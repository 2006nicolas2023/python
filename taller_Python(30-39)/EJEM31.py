km = int(input("Kilómetros recorridos: "))

if km <= 300:
    total = 5000
elif km <= 1000:
    total = 5000 + (km - 300) * 200
else:
    total = 5000 + 700 * 200 + (km - 1000) * 150

print("Total a pagar:", total)

#Kilómetros recorridos: 1200
#Total a pagar: 215000
 