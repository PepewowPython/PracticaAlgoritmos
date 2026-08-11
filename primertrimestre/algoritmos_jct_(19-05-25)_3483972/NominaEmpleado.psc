Proceso NominaEmpleado
	// @autor: Jeremy Chica Tapasco;
	// @fecha: 12/05/2026;
	// @descripcion: Calcular la nomina de un empleado. Si el salario neto;
	//               calculado es menor o igual a $2'000,000 se debe adicionar;
	//               una comisión del 12.5% sobre el salario base;
	// datos: el mes de la nómina, el documento del empleado, el nombre;
	//        del empleado y el salario mensual del empleado. Estos datos;
	//        deben ser ingresados por teclado. salud: 4%, pensión: 4.5%;
	
	Definir mes Como Caracter;
	Definir documento Como Entero;
	Definir nombre Como Caracter;
	Definir salarioBase, salud, pension, deducciones Como Real;
	Definir salarioNeto, comision, totalPagar Como Real;
	
	Escribir "Ingrese el mes de la nómina: ";
	Leer mes;
	Escribir "Ingrese el documento del empleado: ";
	Leer documento;
	Escribir "Ingrese el nombre del empleado: ";
	Leer nombre;
	Escribir "Ingrese el salario mensual del empleado: ";
	Leer salarioBase;
	
	salud <- salarioBase * 0.04;
	pension <- salarioBase * 0.045;
	deducciones <- salud + pension;
	salarioNeto <- salarioBase - deducciones;
	
	comision <- 0;
	Si salarioNeto <= 2000000 Entonces
		comision <- salarioBase * 0.125;
	FinSi;
	
	totalPagar <- salarioNeto + comision;
	
	Borrar Pantalla;
	Escribir "===== COLILLA DE PAGO =====";
	Escribir "Mes: ", mes;
	Escribir "Documento: ", documento;
	Escribir "Nombre: ", nombre;
	Escribir "---------------------------";
	Escribir "Salario Base: $", salarioBase;
	Escribir "Descuento Salud 4%: $", salud;
	Escribir "Descuento Pensión 4.5%: $", pension;
	Escribir "---------------------------";
	Escribir "Salario Neto: $", salarioNeto;
	
	Si comision > 0 Entonces
		Escribir "Comisión 12.5%: $", comision;
	FinSi;
	
	Escribir "---------------------------";
	Escribir "TOTAL A PAGAR: $", totalPagar;
	Escribir "===========================";
	FinProceso

