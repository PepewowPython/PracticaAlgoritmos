Proceso fibonacci
//@autor: Jeremy Chica Tapasco
//@fecha: 02/06/26			
Definir n, i, a, b, c Como Entero;
		
Escribir "Cantidad:";
Leer n;		
a <- 0;
b <- 1;
		
Para i <- 1 Hasta n Hacer
Escribir a;
c <- a + b;
a <- b;
b <- c;
FinPara
		
FinProceso



