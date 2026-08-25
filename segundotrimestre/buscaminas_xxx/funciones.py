#@author: Jeremy Chica Tapasco
#@fecha: 25-08-2026
#@descripcion: Libreria Funciones Buscaminas
from random import randint

def creartablero(filas, columnas):
    tablero = [[0 for i in range(columnas)] for j in range(filas)]
    minas = int((filas * columnas) * 0.25)
    
    mina = 0
    while mina < minas:
        f = randint(0, filas - 1)
        c = randint(0, columnas - 1)
        if tablero[f][c] == 0:
            tablero[f][c] = -1
            mina += 1
    return tablero

def hallarminas(tablero):
#    filas = len(tablero)
#    columnas = len(tablero[0])
    
#    for f in range(filas):
#        for c in range(len(tablero)):
#            for j in range (len(tablero[0])):
#                if tablero[f][c] == -1:
#                    continue
#                else:
#                 tablero[f][c] += contarminas(tablero, i, j)
    tablero [0][0] = minascelda(tablero, 0, 0)
def minascelda (tablero, i, j):
    numero_minas = 0
    
    if (i -1) >= -1:
        if (j -1) == -1:
            if tablero[i-1][j-1] == -1:
                numero_minas += 1
            if tablero[i-1][j+1] == -1:
                numero_minas += 1
            if tablero[i+1][j-1] == -1:
                numero_minas += 1
        elif (j + 1) == len(tablero[0]):
            if tablero[i-1][j-1] == -1:
                numero_minas += 1
            if tablero[i-1][j+1] == -1:
                numero_minas += 1
            if tablero[i+1][j+1] == -1:
                numero_minas += 1
    return numero_minas
        
                
       
    