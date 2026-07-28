Algoritmo Arreglos
	//@Autor: Jeremy Chica Tapasco
	//@Fecha: 16/06/2026
	//@Descripcion: Manejo de arreglos 
	
	Definir a, b, max, min, suma, i, j, vt Como Entero
	Definir prom Como Real;
	Dimension a[10];
	
	max = -999999;
	min = 999999;
	suma = 0
	b = 500;
	
	a[0] = 23;
	a[1] = 55;
	a[2] = 32;
	a[3] = b;
	a[4] = 78;
	a[5] = -38;
	a[6] = 79;
	a[7] = 23;
	a[8] = 108;
	a[9] = -273;	
	
//Recorrido de arreglo
	Para i = 0 hasta 9 Hacer 
		suma = suma + a[i];
		//hallar el maximo
		Si a[i] > max Entonces
			max = a[i];
		FinSi
		//hallar el minimo
		Si a[i] < min Entonces
			min = a[i];
		FinSi
		Escribir a[i], "," Sin Saltar;
	FinPara
	
	Escribir "El valor maximo encontado entre el arreglo es: ", max;
	Escribir "El valor minimo encontado entre el arreglo es: ", min;
	Escribir "La suma de los valores del arreglo es: ", suma; 
	prom = suma / 10;
	Escribir "El promedio de los valores del arreglo es: ", prom;
	
	//Ordenar el arreglo (BORBUJA)
	
	Para i = 0 Hasta 8 Hacer 
		Para j = i Hasta 9 Hacer 
			Si a[j] >= a[i] Entonces
				vt = a[i];
				a[i] = a[j];
				a[j] = vt;
 			FinSi
		FinPara
	FinPara 
	
	Para i = 0 Hasta 9 Hacer
		Escribir a[i], "," Sin Saltar;
	FinPara
	
FinAlgoritmo
