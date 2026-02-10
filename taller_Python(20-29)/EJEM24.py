capital = float(input("Capital invertido: "))
tasa = float(input("Tasa de interés (%): "))

intereses = capital * tasa / 100

if intereses > 7000:
    capital_final = capital + intereses
    print("Intereses generados:", intereses)
    print("Capital final:", capital_final)
else:
    print("Intereses generados:", intereses)
    print("No se reinvierten los intereses")

#Capital invertido: 100000
#Tasa de interés (%): 10
#Intereses generados: 10000.0
#Capital final: 110000.0
