# @author: Jeremy Chica Tapasco
# @fecha: 28/07/2026
# @descripcion: Manejo de arreglos y funciones
#               Manejo de excepciones.
#arreglos []: lista, modificarse
#         (): tupla, no modificable

lista = []
# insertar un dato en la lista
lista.append(45)
lista.append("manzana")


longitud = len(lista)
print(lista, "numero de elementos: ", longitud)

del(lista[1])
longitud = len(lista)
print(lista, "numero de elementos: ", longitud)
# actualizar el primer elemento

lista[0] = -501
longitud = len(lista)
print(lista, "numero de elementos: ", longitud)

# Ejercicio: crea una lista con los numeros del 1 al 10
# 1ra forma 
arreglo = [1,2,3,4,5,6,7,8,9,10]

# 2da forma
arreglo2 = []
for i in range(1, 11):
    arreglo2.append(i)
print(arreglo2)

# 3ra forma
arreglo3 = [i for i in range(1, 100)]

print(arreglo3)

# crear un arreglo con valores numeros aleatorios 100 to 1000
from random import randint
arreglo4 = [randint(100, 1001) for i in range(10)]
print(arreglo4)

arreglo5 = []
for i  in range(10):
    arreglo5.append(randint(100, 1001))
    print(arreglo5)
  


# Mostrar los elementos del medio
# Mostrar eñ arreglo en orden inverso
# Adicionar 100 a los 5 elementos de la mitad
# Mostrar los elementos ordenados descendentemente (de mayor a menor)
# Intercambiar los valores de los elementos
# Mostrar los elementos impares y guardarlos en arreglo llamado impares
# Mostrar los elementos pares y guardarlos en un arreglo llamado pares
# Mostrar los elementos que se pasaron de 1000



# Ejercicio 1: Mostrar el elemento del medio


medio = len(arreglo4) // 2
print("Elemento del" \
"medio:", arreglo4[medio])



# Ejercicio 2: Mostrar el arreglo en orden inverso


print("Arreglo en orden inverso:")
print(arreglo4[::-1])



# Ejercicio 3: Adicionar 100 a los 5 elementos de la mitad


# En un arreglo de 10 elementos son las posiciones 3,4,5,6 y 7
for i in range(3, 8):
    arreglo4[i] += 100

print("Arreglo después de sumar 100 a los 5 elementos de la mitad:")
print(arreglo4)



# Ejercicio 4: Mostrar los elementos ordenados
# descendentemente (de mayor a menor)


print("Arreglo ordenado de mayor a menor:")
print(sorted(arreglo4, reverse=True))


# Ejercicio 5: Intercambiar los valores de los elementos
# (dejar el arreglo en orden opuesto)

for i in range(len(arreglo4) // 2):
    arreglo4[i], arreglo4[-(i + 1)] = arreglo4[-(i + 1)], arreglo4[i]

print("Arreglo con los elementos en orden opuesto:")
print(arreglo4)


# Mostrar los elementos impares y guardarlos en un arreglo llamado impares
# Mostrar los elementos pares y guardarlos en un arreglo llamado pares


impares = []
pares = []

for numero in arreglo4:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Elementos impares:")
print(impares)

print("Elementos pares:")
print(pares)


# Mostrar los elementos que se pasaron de 1000




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

print("Elementos mayores que 1000:")

for valor in arreglo4:
    if valor > 1000:
        print(valor)
