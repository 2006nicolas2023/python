hipoteca = float(input("Monto de la hipoteca: "))
inversion = float(input("Inversión total requerida: "))

if hipoteca < 1_000_000:
    propio = inversion * 0.50
    socio = inversion * 0.50
else:
    propio = hipoteca
    resto = inversion - hipoteca
    socio = resto / 2
    propio += resto / 2

print("Inversión propia:", propio)
print("Inversión del socio:", socio)

#Monto de la hipoteca: 1200000
#Inversión total requerida: 1600000
#Inversión propia: 1400000.0
#Inversión del socio: 200000.0
