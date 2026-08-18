Algoritmo CalculoPrestamo
	// Declaración de variables
	Definir monto, tasaAnual, tasaMensual, cuota, interes, amortizacion, saldo Como Real
	Definir totalIntereses, totalPagar Como Real
	Definir plazoMeses, i, sistema Como Entero

	Escribir "=================================================="
	Escribir "     SIMULADOR DE PRÉSTAMO (FRANCÉS Y ALEMÁN)    "
	Escribir "=================================================="

	// Entrada y validación del monto
	Repetir
		Escribir "Ingrese el monto del préstamo ($): "
		Leer monto
		Si monto <= 0 Entonces
			Escribir "ERROR: El monto debe ser mayor a 0."
		FinSi
	Hasta Que monto > 0

	// Entrada y validación de la tasa anual
	Repetir
		Escribir "Ingrese la tasa de interés anual (%): "
		Leer tasaAnual
		Si tasaAnual <= 0 Entonces
			Escribir "ERROR: La tasa debe ser mayor a 0."
		FinSi
	Hasta Que tasaAnual > 0

	// Entrada y validación del plazo en meses
	Repetir
		Escribir "Ingrese el plazo del préstamo (en meses): "
		Leer plazoMeses
		Si plazoMeses <= 0 Entonces
			Escribir "ERROR: El plazo debe ser mayor a 0."
		FinSi
	Hasta Que plazoMeses > 0

	// Conversión de la tasa de interés anual a tasa mensual decimal
	tasaMensual <- (tasaAnual / 100) / 12

	Escribir ""
	Escribir "Seleccione el sistema de amortización:"
	Escribir "1. Método Francés (Cuota Fija)"
	Escribir "2. Método Alemán (Amortización Fija)"
	Escribir "Opción (1/2): "
	Leer sistema

	Escribir ""
	Escribir "========================================================================="

	totalIntereses <- 0
	totalPagar <- 0
	saldo <- monto

	Segun sistema Hacer
		1:
			Escribir "                     TABLA DE AMORTIZACIÓN - MÉTODO FRANCÉS              "
			Escribir "========================================================================="
			// Método Francés: Cuota fija = P * [ i * (1+i)^n ] / [ (1+i)^n - 1 ]
			cuota <- monto * (tasaMensual * (1 + tasaMensual)^plazoMeses) / (((1 + tasaMensual)^plazoMeses) - 1)

			Escribir "Mes |      Cuota      |     Interés     |   Amortización   |      Saldo      "
			Escribir "-------------------------------------------------------------------------"

			Para i <- 1 Hasta plazoMeses Hacer
				interes <- saldo * tasaMensual
				amortizacion <- cuota - interes
				saldo <- saldo - amortizacion
				
				Si saldo < 0 Entonces
					saldo <- 0
				FinSi

				totalIntereses <- totalIntereses + interes
				totalPagar <- totalPagar + cuota

				Escribir i, "   | $", Redondear(cuota * 100) / 100, " | $", Redondear(interes * 100) / 100, " | $", Redondear(amortizacion * 100) / 100, " | $", Redondear(saldo * 100) / 100
			FinPara

		2:
			Escribir "                     TABLA DE AMORTIZACIÓN - MÉTODO ALEMÁN               "
			Escribir "========================================================================="
			// Método Alemán: Amortización constante del capital = P / n
			amortizacion <- monto / plazoMeses

			Escribir "Mes |      Cuota      |     Interés     |   Amortización   |      Saldo      "
			Escribir "-------------------------------------------------------------------------"

			Para i <- 1 Hasta plazoMeses Hacer
				interes <- saldo * tasaMensual
				cuota <- amortizacion + interes
				saldo <- saldo - amortizacion

				Si saldo < 0 Entonces
					saldo <- 0
				FinSi

				totalIntereses <- totalIntereses + interes
				totalPagar <- totalPagar + cuota

				Escribir i, "   | $", Redondear(cuota * 100) / 100, " | $", Redondear(interes * 100) / 100, " | $", Redondear(amortizacion * 100) / 100, " | $", Redondear(saldo * 100) / 100
			FinPara

		De Otro Modo:
			Escribir "Opción inválida. Debe elegir 1 o 2."
	FinSegun

	Si sistema = 1 O sistema = 2 Entonces
		Escribir "-------------------------------------------------------------------------"
		Escribir "TOTAL INTERESES PAGADOS : $", Redondear(totalIntereses * 100) / 100
		Escribir "TOTAL GENERAL A PAGAR   : $", Redondear(totalPagar * 100) / 100
		Escribir "========================================================================="
	FinSi

FinAlgoritmo
