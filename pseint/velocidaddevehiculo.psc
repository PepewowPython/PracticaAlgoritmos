// @autor: Jeremy Chica Tapasco;
// @fecha: 12/05/2026;
// @descripcion: Calcular la velocidad de un vehiculo.
// datos: la velocidad, el tiempo y la distancia.
Proceso velocidaddevehiculo
	Definir x,t Como Real;
	Definir v Como Real;
	Escribir ("ingrese la distancia recorrida: ");
	Leer x;
	Escribir("Ingrese el tiempo en horas:");
	Leer t;
	
	v = x/t;
	si (v > 60) Entonces
		Escribir "Exceso de velocidad";
	SiNo
		Escribir "No hay exceso";
	FinSi
	
	Escribir "Su velocidad es de: ",v,"(KM/h)";
FinProceso
