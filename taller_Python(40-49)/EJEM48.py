print("F\tC\tK\tR")
print("-" * 40)

# Rango 1: 28 a 54
for F in range(28, 55):
    C = 5 * (F - 32) / 9
    K = C + 273.15
    R = F + 459.67
    print(f"{F}\t{C:.2f}\t{K:.2f}\t{R:.2f}")

print("\nF\tC\tK\tR")
print("-" * 40)

# Rango 2: 450 a 950
for F in range(450, 951, 50):
    C = 5 * (F - 32) / 9
    K = C + 273.15
    R = F + 459.67
    print(f"{F}\t{C:.2f}\t{K:.2f}\t{R:.2f}")

print("\nF\tC\tK\tR")
print("-" * 40)

# Rango 3: -50 a 250
for F in range(-50, 251, 10):
    C = 5 * (F - 32) / 9
    K = C + 273.15
    R = F + 459.67
    print(f"{F}\t{C:.2f}\t{K:.2f}\t{R:.2f}")

#F	C	K	R
#----------------------------------------
#28	-2.22	270.93	487.67
#29	-1.67	271.48	488.67
#30	-1.11	272.04	489.67
#...
