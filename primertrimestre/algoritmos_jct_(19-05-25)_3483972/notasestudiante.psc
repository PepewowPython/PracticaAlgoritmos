Proceso notasestudiante
	Definir n1,n2,n3,n4,def Como Real;
	Definir doc Como Caracter;
	Definir nom Como Caracter;	
	
	Escribir "Ingrese Nombre del Estudiante";
	Leer nom;
	Escribir "Documento:";
	Leer doc;
	Escribir "Ingrese nota 1";
	Leer n1;
	Escribir "Ingrese nota 2";
	Leer n2;
	Escribir "Ingrese nota 3";
	Leer n3;
	Escribir "Ingrese nota 4";
	Leer n4;
	
	def = (n1+n2+n3+n4)/4;
	
	Escribir "BOLETÍN DE CALIFICACIONES";
	Escribir doc;
	Escribir nom;
	Escribir n1,"/",n2,"/",n3,"/",n4;
	Escribir def;
	
	
	
FinProceso
