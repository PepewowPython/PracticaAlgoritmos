"""
@autor: Jeremy Chica Tapasco
@fecha: 19/05/2026
@descripcion: Realizar un Algoritmo que lea una nota definitiva
y asigne un desempeño según el rango:
- bajo (de 0 a 2.9)
- basico (de 3.0 a 3.9)
- alto (de 4.0 a 4.5)
- superior (de 4.5 a 5.0)

se debe ingresar el documento del estudiante.
                     el nombre del estudiante
                     el periodo del informe
                     el nombre de la materia
                     la nota definitiva
"""
# entrada
doc = input("Ingrese el documento del estudiante: ")
nom = input("Ingrese el nombre del estudiante: ")
per = int(input("Ingrese el periodo del informe del estudiante: "))
mat = input("Ingrese la materia cursada del estudiante: ")
Nota = float(input("Ingrese la nota definitiva del estudiante: "))

# lógica if-else anidada
if Nota >= 0 and Nota <= 2.9:
    mensaje = "Bajo"
elif Nota >= 3.0 and Nota <= 3.9:
    mensaje = "Básico"
elif Nota >= 4.0 and Nota <= 4.5:
    mensaje = "Alto"
elif Nota > 4.5 and Nota <= 5.0:
    mensaje = "Superior"
else:
    mensaje = "Nota inválida"

print("------------------------------------------------")
print(f"| REPORTE DE CALIFICACIONES PERIODO: {per} \t|")
print("+------------------------------------------------+")
print(f"| Documento: {doc} \t\t\t\t|")
print(f"| Nombre: {nom} \t\t\t\t|")
print(f"| Materia: {mat} \t\t\t\t|")
print(f"| Nota Definitiva: {Nota} \t\t\t\t|")
print(f"| Desempeño: {mensaje} \t\t\t\t|")
print("------------------------------------------------")
