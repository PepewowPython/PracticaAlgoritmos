# @autor: Jeremy Chica Tapasco
# @fecha: 19/05/2026
# @descripcion: Realizar un Algoritmo para calcular la nomina de un empleado

documento = input("Ingrese el documento del empleado: ")
nombre = input("Ingrese el nombre del empleado: ")
mes = input("Ingrese el mes de la nomina: ")
salarioBase = float(input("Ingrese el salario base: "))

salud = salarioBase * 0.04
pension = salarioBase * 0.045

salarioNeto = salarioBase - salud - pension

if salarioBase < 2000000:
    comision = salarioNeto * 0.20
else:
    comision = salarioNeto * 0.075

totalPagar = salarioNeto + comision

print("------------------------------------------------")
print("| REPORTE DE NOMINA EMPLEADO:                  |")
print("+------------------------------------------------+")
print("| Documento:", documento)
print("| Nombre:", nombre)
print("| Mes:", mes)
print("| Salud:", salud)
print("| Pension:", pension)
print("| Salario neto:", salarioNeto)
print("| Comision:", comision)
print("| Total a pagar:", totalPagar)
print("------------------------------------------------")