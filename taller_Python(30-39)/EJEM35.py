temp = float(input("Temperatura en Fahrenheit: "))

if temp < 50:
    deporte = "Esquí"
elif temp <= 70:
    deporte = "Fútbol"
elif temp <= 85:
    deporte = "Tenis"
else:
    deporte = "Natación"

print("Deporte recomendado:", deporte)

#Temperatura en Fahrenheit: 80
#Deporte recomendado: Tenis
