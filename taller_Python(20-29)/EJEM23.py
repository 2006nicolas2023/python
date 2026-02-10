M = int(input("Kg de harina: "))
N = int(input("Litros de aceite: "))
B1 = float(input("Precio bulto harina: "))
B2 = float(input("Precio caja aceite: "))
B3 = float(input("Precio harina al detal: "))
B4 = float(input("Precio aceite al detal: "))


bultos = M // 24
resto_harina = M % 24
cajas = N // 15
resto_aceite = N % 15


ingreso = (bultos * B1) + (cajas * B2) + (resto_harina * B3) + (resto_aceite * B4)
print("Ingreso total:", ingreso)


#452
#197
#132
#180
#7.5
#14.5
#Ingreso total: 4895.0