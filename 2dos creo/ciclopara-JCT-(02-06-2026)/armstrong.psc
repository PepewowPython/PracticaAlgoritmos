Proceso armstrong
	//@autor: Jeremy Chica Tapasco
	//@fecha: 02/06/2026
	// @Descripción:
	// Dentro del contexto de las matemáticas recreativas se encuentra
	// el concepto de número de Armstrong, también conocido como
	// número narcisista; definido como aquel en que la suma de cada
	// una de sus cifras elevadas a la potencia n es igual a él mismo,
	// donde n está dada por la cantidad de cifras o dígitos del número.
	//
	// Por ejemplo, el número 407, que posee 3 cifras, es un Armstrong:
	// 4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407
	//
	// Construya un algoritmo que reciba un número entero positivo
	// en base 10 y determine si es o no un número de Armstrong.
	
	Proceso Armstrong
		
		Definir numero, copia, cantidad, suma, cifra Como Entero
		
		Escribir "Numero:"
		Leer numero
		
		copia <- numero
		cantidad <- 0
		
		Mientras copia > 0 Hacer
			cantidad <- cantidad + 1
			copia <- Trunc(copia / 10)
		FinMientras
		
		copia <- numero
		suma <- 0
		
		Mientras copia > 0 Hacer
			
			cifra <- copia - Trunc(copia / 10) * 10
			suma <- suma + cifra^cantidad
			
			copia <- Trunc(copia / 10)
			
		FinMientras
		
		Si suma = numero Entonces
			Escribir "Es Armstrong"
		Sino
			Escribir "No es Armstrong"
		FinSi

FinProceso

FinProceso
