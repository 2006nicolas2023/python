suma = 0
k = 1

while True:
    termino = (k**2 + 1) / k
    if suma + termino > 1000:
        break
    suma += termino
    k += 1

print("Número de términos:", k - 1)
print("Valor de la sumatoria:", suma)

#Número de términos: 43
#Valor de la sumatoria: 987.18
