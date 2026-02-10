from datetime import date

anio = int(input("Año de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
dia = int(input("Día de nacimiento: "))

hoy = date.today()
edad = hoy.year - anio

if (mes, dia) > (hoy.month, hoy.day):
    edad -= 1

print("Edad:", edad)
print("Signo: Aries (ejemplo)")

#Año de nacimiento: 2000
#Mes de nacimiento: 5
#Día de nacimiento: 10
#Edad: 25
#Signo: Aries (ejemplo)
