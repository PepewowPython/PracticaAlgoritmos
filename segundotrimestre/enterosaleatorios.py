#@descripción: crear una lista con 10 numeros aleatorios entre 100 y 1000
from random import randint
lista=[randint(100,1001) for i in range (10)]
for i in range(10):
    lista.append(randint(100,1001))
#recorrido
for i in range (len(lista)):
    print (f"elemento{i+1}:{lista[1]}")

#los ultimos 5
print (lista[-5:])
#los 5 primeros
print (lista[0:5])
print("elementos del medio",lista [3:7])
print ("arreglo inverso: ", lista[::-1])

for valor in lista:
    if valor > 1000:
        print (valor)
        
for i in range (len(lista)):
    if lista [i]> 1000:
        print (lista [i])
