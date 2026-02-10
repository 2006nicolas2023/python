n = int(input("Cantidad empresas: "))

agricolas = 0
mineras_sur = 0
total_mineras = 0

trab_agri = trab_miner = trab_ind = 0
cont_agri = cont_miner = cont_ind = 0
ind_norte = ind_sur = 0

for i in range(n):
    actividad = input("Actividad (A/M/I): ")
    zona = input("Zona (N/S): ")
    trab = int(input("Trabajadores: "))

    if actividad == "A":
        agricolas += 1
        trab_agri += trab
        cont_agri += 1
    elif actividad == "M":
        total_mineras += 1
        trab_miner += trab
        cont_miner += 1
        if zona == "S":
            mineras_sur += 1
    elif actividad == "I":
        trab_ind += trab
        cont_ind += 1
        if zona == "N":
            ind_norte += 1
        else:
            ind_sur += 1

print("Porcentaje agrícolas:", (agricolas/n)*100)
print("Porcentaje mineras del sur:", (mineras_sur/total_mineras)*100)
print("Promedio trabajadores agrícolas:", trab_agri/cont_agri)
print("Promedio trabajadores mineras:", trab_miner/cont_miner)
print("Promedio trabajadores industriales:", trab_ind/cont_ind)

if ind_norte > ind_sur:
    print("Zona con más industriales: Norte")
else:
    print("Zona con más industriales: Sur")


#Cantidad empresas: 2
#Actividad (A/M/I): A
#Zona (N/S): N
#Trabajadores: 10
#Actividad (A/M/I): M
#Zona (N/S): S
#Trabajadores: 20
#Porcentaje agrícolas: 50.0
#Porcentaje mineras del sur: 100.0
#Promedio trabajadores agrícolas: 10.0
#Promedio trabajadores mineras: 20.0
#Promedio trabajadores industriales: 0
#Zona con más industriales: Sur
