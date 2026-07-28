// @Descripción: Realizar un algoritmo que lea una serie de puntajes de
//               un juego y almacene los 10 primeros mejores puntajes.
//               Los puntajes deben ser leídos por teclado y se debe
//               realizar la validación de estos por medio de una función.
//               Los puntajes deben ser mostrados en orden descendente.
Funcion valido <- ValidarPuntaje(puntaje)
    Definir valido Como Logico
	
    Si puntaje >= 0 Entonces
        valido <- Verdadero
    SiNo
        valido <- Falso
    FinSi
FinFuncion

Proceso MejoresPuntajes
	
    Definir puntajes Como Entero
    Dimension puntajes[10]
	
    Definir i, j, aux, nuevoPuntaje, cantidad Como Entero
	
    // Inicializar arreglo
    Para i <- 1 Hasta 10 Hacer
        puntajes[i] <- -1
    FinPara
	
    Escribir "¿Cuantos puntajes desea ingresar?"
    Leer cantidad
	
    Para i <- 1 Hasta cantidad Hacer
		
        Repetir
            Escribir "Ingrese puntaje ", i, ": "
            Leer nuevoPuntaje
        Hasta Que ValidarPuntaje(nuevoPuntaje)
		
        // Insertar en los 10 mejores
        Para j <- 1 Hasta 10 Hacer
			
            Si nuevoPuntaje > puntajes[j] Entonces
				
                Para aux <- 10 Hasta j + 1 Con Paso -1 Hacer
                    puntajes[aux] <- puntajes[aux - 1]
                FinPara
				
                puntajes[j] <- nuevoPuntaje
                j <- 11
				
            FinSi
			
        FinPara
		
    FinPara
	
    Escribir ""
    Escribir "TOP 10 PUNTAJES"
	
    Para i <- 1 Hasta 10 Hacer
        Si puntajes[i] <> -1 Entonces
            Escribir i, ". ", puntajes[i]
        FinSi
    FinPara
	
FinProceso