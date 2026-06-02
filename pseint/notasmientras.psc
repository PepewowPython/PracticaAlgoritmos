Proceso Notaswhile
	//@autor: Jeremy Chica Tapasco
	//@fecha: 26/05/2026
	//@descripción: Utilización del bloque repetitivo Mientras 
	//Realizar un algoritmo que muestre la nota definitiva de varios
	//estudiantes con el mensaje "APROBADO" o "NO APROBADO" de acuerdo
	//con la nota ingresada.
	//Se debe mostrar el numero  de estudiantes procesados.
	//El algoritmo se termina cuando se ingrese la letra "N" o "n"
	//se debe ingresar por teclado: el documento, el nombre, la materia,y la notadef
	
	Definir documento,nombre,materia,mensaje,respuesta Como Caracter;
	Definir conteoest Como Entero;
	Definir  notadef Como Real;
	conteoest = 0;
	Escribir "Desea Ingresar el Estudiante? [S/n]";
	Leer  respuesta;
	Mientras  respuesta <> "S" y respuesta <>"s" y respuesta <> "N" y respuesta <> "n" Hacer		
		mensaje = "Respuesta no valida";
		Escribir "¿Desea ingresar un estudiante?[S/n]";
		leer respuesta;
	FinMientras
	Mientras respuesta = "S" o respuesta ="s" Hacer		
		Escribir "Ingrese el Doc del estudiante";
		Leer documento;
		Escribir "Ingrese el nombre del estudiante";
		Leer nombre;
		Escribir "Ingrese la materia del estudiante";
		Leer materia;
		Escribir "Ingrese la nota del estudiante";
		Leer notadef;
		
		si notadef >= 3.5 Entonces			
			mensaje = "APROVADO";
		SiNo
			mensaje = "NO APROVADO";
		FinSi
		
		Escribir "+---------------------------------------------+";
		Escribir "|				   REPORTE DE NOTAS				|";
		Escribir "+---------------------------------------------+";
		Escribir "| Documento: ",documento, 					"|";
		Escribir "| Nombre: ",nombre,		 					"|";
		Escribir "| materia: ",materia, 						"|";
		Escribir "| Nota_Definitiva: ",notadef,					"|";
		Escribir "|  ",mensaje,				 					"|";
		Escribir "+---------------------------------------------+";
		
		conteoest = conteoest +1;
		Escribir "Desea ingresar otro Estudiante [S/n]";
		Leer respuesta;
		
		Mientras  respuesta <> "S" y respuesta <>"s" y respuesta <> "N" y respuesta <> "n" Hacer		
			mensaje = "Respuesta no valida";
			Escribir "¿Desea ingresar un estudiante?[S/n]";
		FinMientras
	FinMientras
	Escribir  "numero de estudiantes ingresados es de: ", conteoest;
	Escribir "Proceso Finalizado...";
FinProceso
