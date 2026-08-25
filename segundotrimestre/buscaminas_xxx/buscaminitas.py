#@author: Jeremy Chica Tapasco
#@fecha: 25-08-2026
#@descripcion: Funciones para el juego de buscaminas
import funciones as fn

print("juego de Buscaminas")
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
tablero = fn.creartablero(filas, columnas)
fn.hallarminas(tablero)
for fila in range(len(tablero)):
    print(tablero[fila])