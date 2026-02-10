auto = float(input("Valor del automóvil: "))
devaluacion = float(input("Devaluación en 3 años: "))
terreno = float(input("Incremento del terreno en 3 años: "))

if devaluacion <= terreno / 2:
    print("Conviene comprar el automóvil")
else:
    print("Conviene comprar el terreno")

#Valor del automóvil: 20000
#Devaluación en 3 años: 3000
#Incremento del terreno en 3 años: 8000
#Conviene comprar el automóvil
