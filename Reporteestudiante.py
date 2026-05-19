"""
@autor: Jeremy Chica Tapasco
@fecha: 19/05/2026
@descripcion: Realizar un Algoritmo que lea una nota definitiva.
si la nota es mayor de 3.5 imprimir el mensajse "APROBADO"
de lo contrario el mensaje "NO APROBADO"
se debe ingresar el documento del estudiante.
	                 el nombre del estudiante
	                 el periodo del informe
					   el nombre de la materia
					   la nota definitiva
"""
    #entrada
doc = input("Ingrese el documento del estudiante: ")
nom = input("Ingrese el nombre del estudiante: ")
per = int(input("Ingrese el periodo del informe del estudiante: "))
mat = input("Ingrese la materia cursada del estudiante: ")
Nota = float(input("Ingrese la nota definitiva del estudiante: "))
	
if (Nota > 3.5):
	mensaje = "Aprobado"
else:
    mensaje = "No aprobado"
	
	
print ("------------------------------------------------")
print (f"| REPORTE DE CALIFICACIONES PERIODO: , {per}, 	|")
print ("+------------------------------------------------+")
print (f"|Documento; {doc}       						|")
print (f"|Nombre; {nom} 		    					|")
print (f"|Materia; {mat} 			    				|")
print (f"|Nota_Definitivo; , {doc}		    	    	|")
print (f"| {mensaje}, ) 					    		|")
print ("------------------------------------------------")