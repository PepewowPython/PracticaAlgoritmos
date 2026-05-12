"""
@author:Jeremy Chica Tapasco
@Fecha:12-05-2026
@Descripcion:Algoritmo que calcula la nomina
"""
documento = input("ingrese el documento del empleado:")
nombre = input("ingrese el nombre del empleado:")
salario_base = input("ingrese el salario base del empleado:")
mes_nomina = input("ingrse el mes del reporte de nomina:")

deduccion_salud = salario_base * .04
deduccion_pension = salario_base * .045

deducciones = deduccion_salud + deduccion_pension

salario_neto = salario_base - deducciones

comision = 0.0
if salario_neto <- 2000000:
    comision = salario_base *.125
print (f"Reporte de nomina del mes de:{mes_nomina}")
print (f"documento:{documento}")
print (f"nombre:{nombre}")
print (f"salario_base: COP${salario_base}")
print (f"deduccion por salud: COP${deduccion_salud}")
print (f"deduccion por pension: COP${deduccion_pension}")
print (f"total deducciones: COP${deducciones}")
print (f"salario neto: COP${salario_neto}")
print (f"comision: COP${comision}")