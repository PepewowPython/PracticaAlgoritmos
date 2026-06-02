Proceso magowhile
//@autor: Jeremy Chica Tapasco
//@fecha: 26-05-26
Definir num Como Entero;
Definir mensaje Como Caracter;
mensaje = "Bienvenido al juego";
num = 8;
Escribir "Ingresa tu numero: ";
Leer num;
Mientras num <> 8 Hacer
	Escribir "Ja estas atrapado en mi bucle";
	Escribir "Intenta de nuevo: ";
	Leer num;
FinMientras
Escribir num;
Escribir "Eres libre.";
FinProceso
