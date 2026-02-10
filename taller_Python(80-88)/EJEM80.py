n = int(input("Personas encuestadas: "))

desemp_sin_ed_25 = {}
total_ciudad = {}
prof_desemp = {}
total_prof = {}

for i in range(n):
    estado = input("Estado: ")
    ciudad = input("Ciudad: ")
    municipio = input("Municipio: ")
    edad = int(input("Edad: "))
    educ = input("Educación (N/B/S/P): ")
    situ = input("Situación (D/E): ")

    total_ciudad[ciudad] = total_ciudad.get(ciudad, 0) + 1

    if situ == "D" and educ == "N" and edad > 25:
        desemp_sin_ed_25[municipio] = desemp_sin_ed_25.get(municipio, 0) + 1

    if educ == "P":
        total_prof[estado] = total_prof.get(estado, 0) + 1
        if situ == "D":
            prof_desemp[estado] = prof_desemp.get(estado, 0) + 1

print("Municipios con desempleados sin educación >25:")
for m in desemp_sin_ed_25:
    print(m, desemp_sin_ed_25[m])

print("Ciudades >50%:")
for c in total_ciudad:
    if desemp_sin_ed_25.get(c, 0) > total_ciudad[c] / 2:
        print(c)

mayor = 0
estado_mayor = ""
for e in total_prof:
    porcentaje = (prof_desemp.get(e, 0) / total_prof[e]) * 100
    if porcentaje > mayor:
        mayor = porcentaje
        estado_mayor = e

print("Estado con más profesionales desempleados:", estado_mayor)


#Personas encuestadas: 1
#Estado: T01
#Ciudad: C01
#Municipio: M01
#Edad: 30
#Educación (N/B/S/P): N
#Situación (D/E): D
#Municipios con desempleados sin educación >25:
#M01 1
#Estado con más profesionales desempleados:
