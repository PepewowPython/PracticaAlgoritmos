// @Descripción: Realizar un algoritmo que simule las operaciones de un
//     cajero automático. El cajero debe realizar las operaciones
//     de: retiro, consignación, transferencia y cambio de clave.
//     se deben almacenar en arreglos diferentes las cuentas,
//     los saldos y las claves.
//     Se debe mostrar un menú principal con las cuatro operaciones y
//     un menú adicional por cada operación.
//     las operaciones se deben realizar para mínimo 10 cuentas.
Proceso CajeroAutomatico
	
	Definir cuentas,claves Como Entero
	Definir saldos Como Real
	Dimension cuentas[10],claves[10],saldos[10]
	
	Definir opcion,cuenta,clave,i,pos Como Entero
	Definir cuentaDestino,posDestino,nuevaClave Como Entero
	Definir monto Como Real
	
	cuentas[1]<-1001
	cuentas[2]<-1002
	cuentas[3]<-1003
	cuentas[4]<-1004
	cuentas[5]<-1005
	cuentas[6]<-1006
	cuentas[7]<-1007
	cuentas[8]<-1008
	cuentas[9]<-1009
	cuentas[10]<-1010
	
	claves[1]<-1111
	claves[2]<-2222
	claves[3]<-3333
	claves[4]<-4444
	claves[5]<-5555
	claves[6]<-6666
	claves[7]<-7777
	claves[8]<-8888
	claves[9]<-9999
	claves[10]<-1010
	
	saldos[1]<-100000
	saldos[2]<-200000
	saldos[3]<-300000
	saldos[4]<-400000
	saldos[5]<-500000
	saldos[6]<-600000
	saldos[7]<-700000
	saldos[8]<-800000
	saldos[9]<-900000
	saldos[10]<-1000000
	
	Repetir
		Escribir "1.Retiro"
		Escribir "2.Consignacion"
		Escribir "3.Transferencia"
		Escribir "4.Cambio de clave"
		Escribir "5.Salir"
		Leer opcion
		
		Segun opcion Hacer
			
			1:
				Escribir "Cuenta:"
				Leer cuenta
				Escribir "Clave:"
				Leer clave
				
				pos<-0
				Para i<-1 Hasta 10 Hacer
					Si cuentas[i]=cuenta Y claves[i]=clave Entonces
						pos<-i
					FinSi
				FinPara
				
				Si pos<>0 Entonces
					Escribir "Monto:"
					Leer monto
					Si monto<=saldos[pos] Entonces
						saldos[pos]<-saldos[pos]-monto
						Escribir "Saldo: ",saldos[pos]
					SiNo
						Escribir "Saldo insuficiente"
					FinSi
				SiNo
					Escribir "Datos incorrectos"
				FinSi
				
			2:
				Escribir "Cuenta:"
				Leer cuenta
				
				pos<-0
				Para i<-1 Hasta 10 Hacer
					Si cuentas[i]=cuenta Entonces
						pos<-i
					FinSi
				FinPara
				
				Si pos<>0 Entonces
					Escribir "Monto:"
					Leer monto
					saldos[pos]<-saldos[pos]+monto
					Escribir "Saldo: ",saldos[pos]
				SiNo
					Escribir "Cuenta no encontrada"
				FinSi
				
			3:
				Escribir "Cuenta origen:"
				Leer cuenta
				Escribir "Clave:"
				Leer clave
				
				pos<-0
				Para i<-1 Hasta 10 Hacer
					Si cuentas[i]=cuenta Y claves[i]=clave Entonces
						pos<-i
					FinSi
				FinPara
				
				Si pos<>0 Entonces
					Escribir "Cuenta destino:"
					Leer cuentaDestino
					
					posDestino<-0
					Para i<-1 Hasta 10 Hacer
						Si cuentas[i]=cuentaDestino Entonces
							posDestino<-i
						FinSi
					FinPara
					
					Si posDestino<>0 Entonces
						Escribir "Monto:"
						Leer monto
						
						Si monto<=saldos[pos] Entonces
							saldos[pos]<-saldos[pos]-monto
							saldos[posDestino]<-saldos[posDestino]+monto
							Escribir "Transferencia realizada"
						SiNo
							Escribir "Saldo insuficiente"
						FinSi
					SiNo
						Escribir "Cuenta destino no existe"
					FinSi
				SiNo
					Escribir "Datos incorrectos"
				FinSi
				
			4:
				Escribir "Cuenta:"
				Leer cuenta
				Escribir "Clave actual:"
				Leer clave
				
				pos<-0
				Para i<-1 Hasta 10 Hacer
					Si cuentas[i]=cuenta Y claves[i]=clave Entonces
						pos<-i
					FinSi
				FinPara
				
				Si pos<>0 Entonces
					Escribir "Nueva clave:"
					Leer nuevaClave
					claves[pos]<-nuevaClave
					Escribir "Clave actualizada"
				SiNo
					Escribir "Datos incorrectos"
				FinSi
				
			5:
				Escribir "Fin del programa"
				
		FinSegun
		
	Hasta Que opcion=5
	
FinProceso

