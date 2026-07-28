Proceso Abecedario_Invertido
	//@autor: Jeremy Chica Tapasco
	
	//@Fecha 09/06/2026
	
	//@Elabore un Algoritmo que genere e imprima las letras del abecedario de la siguiente forma
	
	//ZY	
	//ZYXW
	
	//ZYXWV
	
	//ZYXWVU
	
	//ZYXWVUT
	
	//ZYXWVUTS
	
	//ZYXWVUTSR
	
	//ZYXWVUTSRQ
	
	//ZYXWVUTSRQP	
	
	//ZYXWVUTSRQPO
	
	//ZYXWVUTSROPON
	
	//ZYXWVUTSROPONM
	
	//ZYXWVUTSROPONML
	
	//ZYXWVUTSROPONMLK
	
	//ZYXWVUTSRQPONMLKJ
	
	//ZYXWVUTSRQPONMLKJI
	
	//ZYXWVUTSRQPONMLKJIH
	
	//ZYXWVUTSRQPONMLKJIHG
	
	//ZYXWVUTSROPONMLKJIHGF
	
	//ZYXWVUTSRQPONMLKJIHGFE
	
	//ZYXWVUTSRQPONMLKJIHGFED
	
	//ZYXWVUTSRQPONMLKJIHGFEDC
	
	//ZYXWVUTSRQPONMLKJIHGFEDCB
	
	//ZYXWVUTSRQPONMLKJIHGFEDCBA	
	Definir letras Como Cadena;
	Definir i,j Como Entero;
	
	letras <- "ZYXWVUTSRQPONMLKJIHGFEDCBA";
	
	Para i<-1 Hasta Longitud(letras) Hacer
		
		Para j<-1 Hasta i Hacer
			
			Escribir Sin Saltar SubCadena(letras,j,j)," ";
		FinPara
		Escribir "";
	FinPara
	
FinProceso