#@descripción: crear una lista con 10 numeros aleatorios entre 100 y 1000
from random import randinit
lista=[randinit(100,1001) for i in range (10)]

lista2=[]
for i in range(10):
    lista2.append(randinit(100,1001))
#recorrido
for i in range (len(lista)):
    print (f"elemento{i+1}:{lista[1]}")

#los ultimos 5
print (lista[-5:])
#los 5 primeros
print (lista[0:5])