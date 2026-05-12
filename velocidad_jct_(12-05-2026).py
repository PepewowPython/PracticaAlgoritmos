"""
@author: Jeremy Chica Tapasco
@fecha: 12/05/2026
@descripcion: Algoritmo que calcula la velocidad de un vehiculo.
"""
x = float(input("Ingrese la Distancia: "))
t = float(input("Ingrese el tiempo en horas: "))

v = x / t
if v > 60:
    print ("Exceso de Velocidad")

print(f"Su velocidad es: {v} (KM/h)")