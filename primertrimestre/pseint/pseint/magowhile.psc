Proceso magowhile
//@autor: Jeremy Chica Tapasco
//@fecha: 26-05-26
Definir num,count Como Entero;
Definir mensaje Como Caracter;
mensaje = "Bienvenido al juego";
Escribir mensaje;
num = 8;
Escribir "Ingresa tu numero: ";
Leer num;
Mientras num <> 8 Hacer
	Escribir "Ja estas atrapado en mi bucle";
	Escribir "Intenta de nuevo: ";
	Leer num;
	count = count + 1;
FinMientras
Escribir num;
Escribir "Eres libre.";
Escribir "Numero de intentos ",count;
FinProceso
