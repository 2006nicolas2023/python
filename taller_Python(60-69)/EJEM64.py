suma = 0
termino = 1
contador = 0

while suma + termino <= 1.99:
    suma += termino
    termino /= 2
    contador += 1

print("Términos:", contador)
print("Suma:", suma)


#Términos: 8
#Suma: 1.9921875
