Proceso Dimension1
	//@author: Jeremy Chica Tapasco
	//@Fecha: 16/06/20260
	//@Descripción:
	Definir a,b,max,min,suma,i Como Entero;
	Definir prom Como Real;
	Dimensionar a[10];
	max= -9999999;
	min= 999999;
	suma = 0;
	
	b=500;
	a(0) = 23;
	
	a(1) = 55;
	
	a(2) = 32;
	
	a(3) = b;
	
	a(4) = 78;
	
	a(5) = - 38;
	
	a(6) = 79;
	
	a(7) = 23;
	
	a(8) = 108;
	
	a(9) = - 273;
	
	//Recorrido de un arretio
	
	para i=0 hasta 9 Hacer
		
		si a[i]> max Entonces
			max=a[i];
		FinSi
		si a[i] > min Entonces
			min=a[i];
		FinSi		
	FinPara
	Escribir "Valor Maximo: ", max;
	Escribir "Valor minimo: ",min;
	Escribir "valores: ",suma;
	prom= suma/10;
	Escribir "El promedio: ",prom;
	
	para i = 0 Hasta 8 Hacer
		para j = i Hasta 9 Hacer
			si a[j] >= a[i] Entonces
				vt = a[i];
				a[i]=a[j];
				a[j]=vt;				
			FinSi
		FinPara
	FinPara
	para i = 0 Hasta 9 Hacer
		Escribir a[i], "," Sin Saltar;
	FinPara
FinProceso

