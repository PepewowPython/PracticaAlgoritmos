Algoritmo Cajero_Automatico
	//@Autor: Jeremy Chica Tapasco
	//@Fecha: 16/06/2026
	//@Descripcion: 
//	2. Realizar un algoritmo que simule las operaciones de un cajero automatico. El cajero debe realizar las operaciones de:
//	retiro, consignacion, transferencia y cambio de clave, se debn almacenar en arreglos diferentes las cuentas, los saldos y las claves.
//	Se debe mostrar un menu principoal con las cuatro operaciones y un menu adicional por cada operacion 
	
	Definir cuentas, saldos, claves Como Entero
    Dimension cuentas[3]
    Dimension saldos[3]
    Dimension claves[3]
	
    Definir i, cuenta, clave, opcion, pos Como Entero
    Definir monto, nuevaClave Como Real
    Definir encontrada Como Logico
	
    // Datos iniciales
    cuentas[1] <- 1001
    cuentas[2] <- 1002
    cuentas[3] <- 1003
	
    saldos[1] <- 500000
    saldos[2] <- 300000
    saldos[3] <- 200000
	
    claves[1] <- 1234
    claves[2] <- 5678
    claves[3] <- 4321
	
    Escribir "Ingrese su número de cuenta:"
    Leer cuenta
	
    Escribir "Ingrese su clave:"
    Leer clave
	
    encontrada <- Falso
	
    Para i <- 1 Hasta 3 Hacer
        Si cuentas[i] = cuenta Y claves[i] = clave Entonces
            encontrada <- Verdadero
            pos <- i
        FinSi
    FinPara
	
    Si encontrada Entonces
		
        Repetir
			
            Escribir "====== CAJERO AUTOMÁTICO ======"
            Escribir "1. Retiro"
            Escribir "2. Consignación"
            Escribir "3. Transferencia"
            Escribir "4. Cambio de clave"
            Escribir "5. Salir"
            Leer opcion
			
            Segun opcion Hacer
				
                1:
                    Escribir "Ingrese el monto a retirar:"
                    Leer monto
					
                    Si monto <= saldos[pos] Entonces
                        saldos[pos] <- saldos[pos] - monto
                        Escribir "Retiro exitoso."
                        Escribir "Saldo actual: ", saldos[pos]
                    Sino
                        Escribir "Saldo insuficiente."
                    FinSi
					
                2:
                    Escribir "Ingrese el monto a consignar:"
                    Leer monto
					
                    saldos[pos] <- saldos[pos] + monto
					
                    Escribir "Consignación exitosa."
                    Escribir "Saldo actual: ", saldos[pos]
					
                3:
                    Definir cuentaDestino Como Entero
                    Definir destino Como Entero
                    destino <- -1
					
                    Escribir "Ingrese la cuenta destino:"
                    Leer cuentaDestino
					
                    Escribir "Ingrese el monto:"
                    Leer monto
					
                    Para i <- 1 Hasta 3 Hacer
                        Si cuentas[i] = cuentaDestino Entonces
                            destino <- i
                        FinSi
                    FinPara
					
                    Si destino <> -1 Entonces
                        Si monto <= saldos[pos] Entonces
                            saldos[pos] <- saldos[pos] - monto
                            saldos[destino] <- saldos[destino] + monto
                            Escribir "Transferencia realizada."
                        Sino
                            Escribir "Saldo insuficiente."
                        FinSi
                    Sino
                        Escribir "Cuenta destino no existe."
                    FinSi
					
                4:
                    Escribir "Ingrese la nueva clave:"
                    Leer nuevaClave
					
                    claves[pos] <- nuevaClave
					
                    Escribir "Clave cambiada exitosamente."
					
                5:
                    Escribir "Gracias por utilizar el cajero."
					
                De Otro Modo:
                    Escribir "Opción inválida."
					
            FinSegun
			
        Hasta Que opcion = 5
		
    Sino
        Escribir "Cuenta o clave incorrecta."
    FinSi

FinAlgoritmo
