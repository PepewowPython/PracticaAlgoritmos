Proceso Reporteperiodo
	//@autor: Jeremy Chica Tapasco
	//@fecha: 19/05/2026
	//@descripcion: Realizar un Algoritmo que lea una nota definitiva.
	//si la nota es mayor de 3.5 imprimir el mensajse "APROBADO"
	//de lo contrario el mensaje "NO APROBADO"
	//se debe ingresar el documento del estudiante.
	//                 el nombre del estudiante
	//                 el periodo del informe
	//				   el nombre de la materia
	//				   la nota definitiva
	Definir documento, nombre, materia, mensaje  Como Caracter;
	Definir periodo_informe Como Entero;
	Definir nota_definitiva Como Real;
	
	Escribir "Ingrese el documento del estudiante: ";
	Leer  documento ;
	Escribir "Ingrese el nombre del estudiante: ";
	Leer  nombre;
	Escribir "Ingrese el periodo del informe del estudiante: ";
	Leer  periodo_informe;	
	Escribir "Ingrese la materia cursada del estudiante: ";
	Leer  materia;
	Escribir "Ingrese la nota definitiva del estudiante: ";
	Leer  nota_definitiva;
	
	Si (nota_definitiva > 3.5) Entonces
		mensaje = "Aprobado";
	SiNo
		mensaje = "No aprobado";
	FinSi
	
	Escribir "------------------------------------------------";
	Escribir "| REPORTE DE CALIFICACIONES PERIODO: ", periodo_informe, " 	|";
	Escribir "+------------------------------------------------+";
	Escribir "|Documento; ", documento, "						|";
	Escribir "|Nombre; ", nombre, "							|";
	Escribir "|Materia; ", materia, "							|";
	Escribir "|Nota_Definitivo; ", documento, "				|";
	Escribir "|", mensaje, "									|";
	Escribir "------------------------------------------------";
FinProceso

