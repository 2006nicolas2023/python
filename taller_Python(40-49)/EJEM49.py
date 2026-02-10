a = b = c = 0
ab = ac = bc = 0
solo_a = solo_b = solo_c = 0
ninguna = 0

for i in range(1, 101):
    print(f"\nPersona {i}")
    p1 = int(input("Respondió bien P1? (1=Sí, 0=No): "))
    p2 = int(input("Respondió bien P2? (1=Sí, 0=No): "))
    p3 = int(input("Respondió bien P3? (1=Sí, 0=No): "))

    if p1 and p2 and p3:
        a += 1
    elif p1 and p2:
        ab += 1
    elif p1 and p3:
        ac += 1
    elif p2 and p3:
        bc += 1
    elif p1:
        solo_a += 1
    elif p2:
        solo_b += 1
    elif p3:
        solo_c += 1
    else:
        ninguna += 1

print("\nRESULTADOS")
print("Tres correctas:", a)
print("Primera y segunda:", ab)
print("Primera y tercera:", ac)
print("Segunda y tercera:", bc)
print("Al menos la primera:", a + ab + ac + solo_a)
print("Al menos la segunda:", a + ab + bc + solo_b)
print("Al menos la tercera:", a + ac + bc + solo_c)
print("Ninguna correcta:", ninguna)

#Persona 1
#Respondió bien P1? (1=Sí, 0=No): 1
#Respondió bien P2? (1=Sí, 0=No): 1
#Respondió bien P3? (1=Sí, 0=No): 0
#...
#RESULTADOS
#Tres correctas: 12
#Primera y segunda: 18
#Primera y tercera: 15
#Segunda y tercera: 10
#Al menos la primera: 60
#Al menos la segunda: 55
#Al menos la tercera: 48
#Ninguna correcta: 5
