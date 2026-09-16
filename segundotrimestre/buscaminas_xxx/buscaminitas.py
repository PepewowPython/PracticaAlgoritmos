#@author: Jeremy Chica Tapasco
#@fecha: 25-08-2026
#@descripcion: Juego de Buscaminas
import funciones as fn


def partida():
    print("\nJUEGO DE BUSCAMINAS")
    while True:
        try:
            filas = int(input("Filas (1-20): "))
            columnas = int(input("Columnas (1-20): "))
            if 1 <= filas <= 20 and 1 <= columnas <= 20 and filas * columnas > 1:
                break
        except ValueError:
            pass
        print("Introduce dimensiones válidas (el tablero debe tener más de una celda).")

    tablero = fn.hallarminas(fn.creartablero(filas, columnas))
    descubiertas = set()
    banderas = set()
    total_celdas = filas * columnas - sum(fila.count(-1) for fila in tablero)

    while True:
        print("\nComandos: d fila columna (descubrir), f fila columna (bandera), s (salir)")
        fn.mostrartablero(tablero, descubiertas, banderas)
        comando = input("> ").strip().lower().split()
        if comando == ["s"]:
            print("Partida terminada.")
            return
        if len(comando) != 3 or comando[0] not in {"d", "f"}:
            print("Comando no válido.")
            continue
        try:
            fila, columna = int(comando[1]) - 1, int(comando[2]) - 1
        except ValueError:
            print("Las coordenadas deben ser números.")
            continue
        if not (0 <= fila < filas and 0 <= columna < columnas):
            print("La coordenada está fuera del tablero.")
            continue

        posicion = (fila, columna)
        if comando[0] == "f":
            if posicion in descubiertas:
                print("Esa celda ya está descubierta.")
            elif posicion in banderas:
                banderas.remove(posicion)
            else:
                banderas.add(posicion)
        elif posicion in banderas:
            print("Quita la bandera antes de descubrir esa celda.")
        elif not fn.descubrir(tablero, descubiertas, fila, columna):
            print("\n¡Has pisado una mina!")
            fn.mostrartablero(tablero, descubiertas, banderas, revelar_minas=True)
            return

        if len(descubiertas) == total_celdas:
            print("\n¡Has ganado!")
            fn.mostrartablero(tablero, descubiertas, banderas)
            return


if __name__ == "__main__":
    partida()
