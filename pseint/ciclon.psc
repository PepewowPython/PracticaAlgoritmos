Proceso ciclon
// @Autor: Jeremy Chica Tapasco
// @Fecha:02/06/2026
// @Descripcion: Realizar un Algoritmo  que imprima los n primeros numeros naturales
	
Definir  i, n Como Entero;
	
Escribir "Ingrese el numero natural hasta el cual desea imprimir: ";
Leer n;
	
Mientras n <= 0 Hacer
	Escribir "EL numero ingresado no es un numero natural...";
	Escribir "Ingrese el numero natural hasta el cual desea imprimir:";
	Leer n;
FinMientras
	
para i = 1 hasta n Hacer
	Escribir i;
FinPara
	
FinProceso
