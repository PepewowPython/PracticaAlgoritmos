#@author: Jeremy Chica Tapasco
#@fecha: 25-08-2026
#@descripcion: Libreria Funciones Buscaminas
from random import sample


def creartablero(filas, columnas):
    if filas < 1 or columnas < 1:
        raise ValueError("El tablero debe tener al menos una fila y una columna")
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    minas = max(1, min((filas * columnas) // 4, filas * columnas - 1))
    for posicion in sample(range(filas * columnas), minas):
        tablero[posicion // columnas][posicion % columnas] = -1
    return tablero


def hallarminas(tablero):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] != -1:
                tablero[fila][columna] = minascelda(tablero, fila, columna)
    return tablero


def minascelda(tablero, fila, columna):
    return sum(
        0 <= vecino_fila < len(tablero)
        and 0 <= vecino_columna < len(tablero[0])
        and tablero[vecino_fila][vecino_columna] == -1
        for vecino_fila in range(fila - 1, fila + 2)
        for vecino_columna in range(columna - 1, columna + 2)
        if (vecino_fila, vecino_columna) != (fila, columna)
    )


def mostrartablero(tablero, descubiertas=None, banderas=None, revelar_minas=False):
    descubiertas = descubiertas or set()
    banderas = banderas or set()
    columnas = len(tablero[0])
    print("    " + " ".join(f"{columna + 1:2}" for columna in range(columnas)))
    for fila, contenido in enumerate(tablero):
        celdas = []
        for columna, valor in enumerate(contenido):
            posicion = (fila, columna)
            if posicion in banderas:
                celda = "F"
            elif posicion not in descubiertas and not (revelar_minas and valor == -1):
                celda = "#"
            elif valor == -1:
                celda = "*"
            else:
                celda = str(valor)
            celdas.append(f"{celda:>2}")
        print(f"{fila + 1:2}  " + " ".join(celdas))


def descubrir(tablero, descubiertas, fila, columna):
    if tablero[fila][columna] == -1:
        return False
    pendientes = [(fila, columna)]
    while pendientes:
        actual_fila, actual_columna = pendientes.pop()
        if (actual_fila, actual_columna) in descubiertas:
            continue
        descubiertas.add((actual_fila, actual_columna))
        if tablero[actual_fila][actual_columna] == 0:
            for vecino_fila in range(actual_fila - 1, actual_fila + 2):
                for vecino_columna in range(actual_columna - 1, actual_columna + 2):
                    if (0 <= vecino_fila < len(tablero)
                            and 0 <= vecino_columna < len(tablero[0])):
                        pendientes.append((vecino_fila, vecino_columna))
    return True
