Algoritmo N_Numeros_Enteros
	//@Autor: Jeremy Chica Tapasco
	//@Fecha: 16/06/2026
	//@Descripcion:
//	1. Desarrollar un algoritmo que almacene n numero enteros en un arreglo y que posteriormente determine si un numero cualquiera ingresado por el usuario 
//	se encuentra o no en el arreglo. Si el numero se encuentra en el arreglo, el algoritmo debe decir en que posicion esta.

	Definir n, i, numero, posicion Como Entero
    Definir encontrado Como Logico
    Definir arreglo Como Entero
	
    Escribir "¿Cuántos números desea ingresar?"
    Leer n
	
    Dimension arreglo[n]
	
    Para i <- 1 Hasta n Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer arreglo[i]
    FinPara
	
    Escribir "Ingrese el número que desea buscar:"
    Leer numero
	
    encontrado <- Falso
	
    Para i <- 1 Hasta n Hacer
        Si arreglo[i] = numero Entonces
            encontrado <- Verdadero
            posicion <- i
        FinSi
    FinPara
	
    Si encontrado Entonces
        Escribir "El número se encuentra en la posición ", posicion
    Sino
        Escribir "El número no se encuentra en el arreglo."
    FinSi
	
FinAlgoritmo
