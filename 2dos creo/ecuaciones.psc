Proceso Ecucaciones
	//@autor: Jeremy Chica Tapasco
	//@Fecha: 02/06/2026
	// @Descripción: Realizar un algoritmo que halle las raíces de la ecuación
	// Ax^2 + Bx + C = 0 en todos los conjuntos numéricos.
	//
	// Fórmula:
	// x = (-B ± raiz(B^2 - 4AC)) / 2A
	
	Proceso RaicesCuadratica
		
		Definir A, B, C, D, x1, x2 Como Real
		
		Escribir "A:"
		Leer A
		
		Escribir "B:"
		Leer B
		
		Escribir "C:"
		Leer C
		
		D <- B^2 - 4*A*C
		
		Si D >= 0 Entonces
			x1 <- (-B + Raiz(D)) / (2*A)
			x2 <- (-B - Raiz(D)) / (2*A)
			
			Escribir "x1 = ", x1
			Escribir "x2 = ", x2
		Sino
			Escribir "Raices complejas"
		FinSi
		
FinProceso

