Proceso trescolumnas
	//@autor:Jeremy Chica Tapasco
	//@fecha: 02/06/2026
	// @Descripción: Construya un algoritmo que imprima tres columnas
	// de números, conforme a la tabla siguiente, en donde el valor de n será
	// proporcionado por el usuario.
	//
	// ----------------
	// 1    1    2
	// 2    4    6
	// 3    9    12
	// 4    16   20
	// 5    25   30
	// .    .    .
	// n    .    .
	// ----------------
	
	Proceso TresColumnas
		
		Definir n, i Como Entero
		
		Escribir "n:"
		Leer n
		
		Para i <- 1 Hasta n Hacer
			Escribir i, "    ", i^2, "    ", i*(i+1)
		FinPara
		
FinProceso