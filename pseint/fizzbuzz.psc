Proceso fizzbuzz
	
    Definir num Como Entero;
	
    num = 1;
	
    Repetir
		
        Si num mod 3 = 0 Y num mod 5 = 0 Entonces
            Escribir "fizzbuzz";
        Sino
            Si num mod 3 = 0 Entonces
                Escribir "fizz";
            Sino
                Si num mod 5 = 0 Entonces
                    Escribir "buzz";
                Sino
                    Escribir num;
                FinSi
            FinSi
        FinSi
		
        num = num + 1;
		
    Hasta Que num > 100
	
FinProceso