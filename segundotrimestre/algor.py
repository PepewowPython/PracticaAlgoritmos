# Autor: Samuel Yate
# Fecha: 28/07/26
# Gruk guardar datos y contar

lista = []
# Meter datos
lista.append(45)
lista.append("manzana")

longitud = len(lista)
print(lista, "total:", longitud)

# Quitar segundo dato
del(lista[1])
longitud = len(lista)
print(lista, "total:", longitud)

# Cambiar primer dato
lista[0] = -501
longitud = len(lista)
print(lista, "total:", longitud)

# Hacer lista del 1 al 10
# Forma 1: Directo
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Forma 2: Con bucle
arreglo2 = []
for i in range(1, 11):
    arreglo2.append(i)
print(arreglo2)

# Forma 3: Bucle corto
arreglo3 = [i for i in range(1, 100)]
print(arreglo3)

# Numeros al azar entre 100 y 1000
from random import randint
arreglo4 = [randint(100, 1001) for i in range(10)]
print(arreglo4)

arreglo5 = []
for i in range(10):
    arreglo5.append(randint(100, 1001))
    print(arreglo5)

# Tarea 1: Ver medio
medio = len(arreglo4) // 2
print("Medio:", arreglo4[medio])

# Tarea 2: Ver al reves
print("Al reves:")
print(arreglo4[::-1])

# Tarea 3: Sumar 100 a los 5 del centro
for i in range(3, 8):
    arreglo4[i] += 100

print("Sumar 100 al centro:")
print(arreglo4)

# Tarea 4: Mayor a menor
print("Mayor a menor:")
print(sorted(arreglo4, reverse=True))

# Tarea 5: Voltear posiciones
for i in range(len(arreglo4) // 2):
    arreglo4[i], arreglo4[-(i + 1)] = arreglo4[-(i + 1)], arreglo4[i]

print("Invertido:")
print(arreglo4)

# Separar par e impar
impares = []
pares = []

for numero in arreglo4:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Impares:", impares)
print("Pares:", pares)

# Buscar mayores a 1000
pares = []
impares = []

for numero in arreglo4:
    if numero > 1000:
        print(numero)

for valor in arreglo4:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Pares:", pares)
print("Impares:", impares)

print("Mayores a 1000:")
for valor in arreglo4:
    if valor > 1000:
        print(valor)
