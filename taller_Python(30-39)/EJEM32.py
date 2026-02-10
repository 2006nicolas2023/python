P = int(input("P: "))
Q = int(input("Q: "))

resultado = P**3 + Q**4 - 2 * P**2

if resultado > 680:
    print("Se cumple la expresión")
    print("P:", P)
    print("Q:", Q)
else:
    print("No se cumple la expresión")

#P: 4
#Q: 3
#Se cumple la expresión
#P: 4
#Q: 3
