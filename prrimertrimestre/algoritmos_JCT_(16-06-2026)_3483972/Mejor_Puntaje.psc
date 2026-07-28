Algoritmo sin_titulo
	//@Autor: Jeremy Chica Tapasco
	//@Fecha: 16/06/2026
	//@Descripcion: Realizar algortimo que lea una serie de puntajes de juego y alcanse los 10 primeros
	// puntajes. Los puntajes deben ser leidos por tecladpo y se debe realizar la validacion de estos por medio de una funcion.
	// Los puntajes deben ser mostrados en orden descendentes 
	Definir puntajes Como Entero
    Dimension puntajes[10];
    Definir i, j, aux , puntaje Como Entero
    
    para i <- 1  hasta 10 Hacer
        Repetir
            Escribir " Ingrese el puntaje"  i,":"
            leer puntaje 
        hasta que ValidarPuntaje(puntaje)
        puntajes[i] <- puntaje
    FinPara
    
    Para i <- 1 Hasta 9 Hacer
        Para j <- 1 +1 hasta 10 Hacer
            si puntajes[i] < puntajes[j] Entonces
                
                aux <- puntajes[i]
                puntajes[i] <- puntajes[j]
                puntajes[j] <- aux
            FinSi
        FinPara
    FinPara
    
    Escribir ""
    Escribir "Top 10 mejores puntajes"
    para i <- 1 hasta 10 Hacer
        Escribir i, ", " , puntajes[i]
    FinPara
FinProceso
Funcion valido <- validarPuntaje(p)
    Definir valido Como Logico
    si p >= 0 Entonces
        valido <- Verdadero
    SiNo
        Escribir "ERROR : el puntaje no puede ser negativo."
        valido <- falso
    FinSi
FinFuncion

