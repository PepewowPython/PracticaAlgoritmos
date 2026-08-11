Proceso nomina
	Definir sal, salud, pension, sal_neto Como Real;
	Definir doc, nom, nombre Como Caracter;
	
	Escribir "Ingrese salario:";
	Leer sal;
	
	Escribir "Ingrese su documento:";
	Leer doc;
	
	Escribir "Ingrese el mes de la nomina:";
	Leer nom;
	
	Escribir "Ingrese su nombre completo:";
	Leer nombre;
	
	// Cálculos correctos
	salud = sal * 0.04;
	pension = sal * 0.04;
	sal_neto = sal - salud - pension;
	
	// Reporte
	Escribir "==============================";
	Escribir "REPORTE DE NOMINA";
	Escribir "Mes: ", nom;
	Escribir "Nombre: ", nombre;
	Escribir "Documento: ", doc;
	Escribir "Salario: ", sal;
	Escribir "Salud (4%): ", salud;
	Escribir "Pension (4%): ", pension;
	Escribir "Salario Neto: ", sal_neto;
	Escribir "==============================";
	
FinProceso
