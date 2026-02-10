hectareas = float(input("Hectáreas del bosque: "))

metros = hectareas * 10000

if metros > 1_000_000:
    pino_m = metros * 0.70
    oyamel_m = metros * 0.20
    cedro_m = metros * 0.10
else:
    pino_m = metros * 0.50
    oyamel_m = metros * 0.30
    cedro_m = metros * 0.20

pinos = int(pino_m / 10 * 8)
oyameles = int(oyamel_m / 15 * 15)
cedros = int(cedro_m / 18 * 10)

print("Pinos:", pinos)
print("Oyameles:", oyameles)
print("Cedros:", cedros)

#Hectáreas del bosque: 150
#Pinos: 840000
#Oyameles: 200000
#Cedros: 83333
