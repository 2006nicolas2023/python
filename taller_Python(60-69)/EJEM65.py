nombre = input("Nombre: ")
cedula = input("Cédula: ")
cargo = input("Cargo (O/A/E): ")
hijos = int(input("Número de hijos: "))
asistencia = float(input("Asistencia (%): "))

if cargo == "O":
    sueldo = 100000
elif cargo == "A":
    sueldo = 165500
else:
    sueldo = 250000

if hijos > 5:
    hijos = 5

asig_hijos = sueldo * 0.10 * hijos
asig_asistencia = sueldo * 0.05 if asistencia > 95 else 0

deduccion_caja = sueldo * 0.10
deduccion_seguro = sueldo * 0.02

sueldo_neto = sueldo + asig_hijos + asig_asistencia - deduccion_caja - deduccion_seguro

print("\nEmpleado:", nombre)
print("Cédula:", cedula)
print("Sueldo básico:", sueldo)
print("Caja de ahorro:", deduccion_caja)
print("Seguro social:", deduccion_seguro)
print("Sueldo neto:", sueldo_neto)

#Nombre: Luis
#Cédula: 123456
#Cargo (O/A/E): O
#Número de hijos: 2
#Asistencia (%): 98

#Empleado: Luis
#Cédula: 123456
#Sueldo básico: 100000
#Caja de ahorro: 10000.0
#Seguro social: 2000.0
#Sueldo neto: 118000.0
