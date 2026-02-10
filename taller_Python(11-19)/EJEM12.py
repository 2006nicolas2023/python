mat = float(input("Examen Matemática: "))
fis = float(input("Examen Física: "))
qui = float(input("Examen Química: "))

prom_mat = mat * 0.9
prom_fis = fis * 0.8
prom_qui = qui * 0.85

prom_general = (prom_mat + prom_fis + prom_qui) / 3

print("Promedio general:", prom_general)

#Examen Matemática: 4.5
#Examen Física: 4.0
#Examen Química: 4.2
#Promedio general: 3.87
